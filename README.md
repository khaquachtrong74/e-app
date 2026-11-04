# e-app — Flask E-commerce Demo

A small Flask shopping app: product listing with search and category filters, user
accounts, and an admin area. Written to try out the Flask stack end to end.

## Stack

Flask · Flask-SQLAlchemy · Flask-Login · MySQL · Jinja2 · Bootstrap

## Structure

```
eapp/
  __init__.py     app + db + login-manager setup
  models.py       BaseModel · User · Category · Product
  dao.py          all queries, kept out of the views
  index.py        routes
  templates/
    index.html            storefront
    layout/{base,header,footer}.html
    admin/index.html      admin area
```

## Routes

| Route | Method | Does |
|---|---|---|
| `/` | GET | storefront; accepts `?kw=` and `?category_id=` for search and filtering |
| `/login-admin` | POST | authenticates, then redirects to `/admin` |

## Notes worth knowing

- **Passwords are stored as unsalted MD5** (`hashlib.md5` in `dao.py`). That is broken —
  it is not slow to brute-force, and identical passwords produce identical hashes. Any real
  deployment needs `werkzeug.security.generate_password_hash` (or bcrypt/argon2). Left as
  a learning-stage artifact, not as a recommendation.
- There is **no `requirements.txt`**; the dependency list has to be inferred from imports.
- `eapp/index.py` starts the app with `debug=True`, which must not be used outside
  development.

## Running

```bash
# needs a MySQL instance and a database matching models.py
pip install flask flask-sqlalchemy flask-login pymysql
python -m eapp.index
```

## Status

Learning project. Not security-reviewed, not deployed.

## License

MIT — see `LICENSE`.
