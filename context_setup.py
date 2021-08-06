from app.routes import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()

print("You have now loaded the context for %s" % current_app.name)
print("*" * 50)
