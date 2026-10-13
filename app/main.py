from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid
import json
import os
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

USERS_FILE = "app/users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {"testuser@shop.com": "Test@123"}

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(USERS, f, indent=2)

USERS = load_users()
SESSIONS = {}
CARTS = {}
ORDERS = {}

PRODUCTS = [
    {"id": 1, "name": "iPhone 15 Pro",    "price": 999.00,  "img": "📱", "cat": "Phones"},
    {"id": 2, "name": "Sony WH-1000XM5",  "price": 349.00,  "img": "🎧", "cat": "Audio"},
    {"id": 3, "name": "MacBook Air M3",   "price": 1199.00, "img": "💻", "cat": "Laptops"},
    {"id": 4, "name": "iPad Air",         "price": 599.00,  "img": "📲", "cat": "Tablets"},
    {"id": 5, "name": "Apple Watch S9",   "price": 399.00,  "img": "⌚", "cat": "Wearables"},
    {"id": 6, "name": "AirPods Pro 2",    "price": 249.00,  "img": "🎵", "cat": "Audio"},
]

VALID_COUPONS   = {"SAVE10": 10}
EXPIRED_COUPONS = {"EXPIRED2020"}
MAX_QTY = 10


def get_session(request):
    sid = request.cookies.get("sid")
    return SESSIONS.get(sid)


def render(name, request, **ctx):
    return templates.TemplateResponse(request=request, name=name, context=ctx)


@app.get("/")
async def home(request: Request):
    return RedirectResponse("/products")


# ---------- REGISTER ----------
@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return render("register.html", request, error=None, user=None)


@app.post("/register")
async def register(request: Request,
                   email: str = Form(...),
                   password: str = Form(...),
                   confirm: str = Form(...)):
    email = email.strip().lower()

    if email in USERS:
        return render("register.html", request, error="Email already registered", user=None)
    if len(password) < 6:
        return render("register.html", request, error="Password must be at least 6 characters", user=None)
    if password != confirm:
        return render("register.html", request, error="Passwords do not match", user=None)

    USERS[email] = password
    save_users()
    CARTS.setdefault(email, [])
    ORDERS.setdefault(email, [])

    return RedirectResponse("/login?registered=1", status_code=302)


# ---------- LOGIN ----------
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, registered: str = ""):
    success = "Account created successfully. Please sign in." if registered else None
    return render("login.html", request, error=None, success=success, user=None)


@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    email = email.strip().lower()
    if USERS.get(email) == password:
        sid = str(uuid.uuid4())
        SESSIONS[sid] = email
        CARTS[email] = []
        ORDERS.setdefault(email, [])
        resp = RedirectResponse("/products", status_code=302)
        resp.set_cookie("sid", sid)
        return resp
    return render("login.html", request, error="Invalid email or password", success=None, user=None)


# ---------- TEST HELPER ----------
@app.get("/__test__/login")
async def test_login(request: Request, email: str):
    email = email.strip().lower()
    if email not in USERS:
        USERS[email] = "Test@123"
        save_users()
    sid = str(uuid.uuid4())
    SESSIONS[sid] = email
    CARTS[email] = []
    ORDERS.setdefault(email, [])
    resp = RedirectResponse("/products", status_code=302)
    resp.set_cookie("sid", sid)
    return resp


@app.get("/logout")
async def logout(request: Request):
    sid = request.cookies.get("sid")
    SESSIONS.pop(sid, None)
    resp = RedirectResponse("/login", status_code=302)
    resp.delete_cookie("sid")
    return resp


# ---------- PRODUCTS ----------
@app.get("/products", response_class=HTMLResponse)
async def products(request: Request, q: str = ""):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    results = [p for p in PRODUCTS if q.lower() in p["name"].lower()] if q else PRODUCTS
    return render("products.html", request, products=results, user=user, q=q)


# ---------- CART ----------
@app.post("/cart/add/{pid}")
async def add_to_cart(request: Request, pid: int, qty: str = Form("1")):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")

    try:
        qty_int = int(qty)
    except ValueError:
        return RedirectResponse("/products?error=invalid_qty", status_code=302)

    if qty_int < 1 or qty_int > MAX_QTY:
        return RedirectResponse("/products?error=invalid_qty", status_code=302)

    product = next((p for p in PRODUCTS if p["id"] == pid), None)
    if product:
        cart = CARTS.setdefault(user, [])
        existing = next((i for i in cart if i["id"] == pid), None)
        if existing:
            existing["qty"] = qty_int
        else:
            cart.append({"id": pid, "name": product["name"], "price": product["price"], "qty": qty_int})
    return RedirectResponse("/cart", status_code=302)


@app.get("/cart", response_class=HTMLResponse)
async def cart(request: Request):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    items = CARTS.get(user, [])
    subtotal = sum(i["price"] * i["qty"] for i in items)
    return render("cart.html", request, items=items, subtotal=round(subtotal, 2), user=user)


@app.post("/cart/remove/{pid}")
async def remove_from_cart(request: Request, pid: int):
    # 🐛 DELIBERATE BUG: does nothing — item stays in cart
    return RedirectResponse("/cart", status_code=302)


# ---------- CHECKOUT ----------
@app.get("/checkout", response_class=HTMLResponse)
async def checkout(request: Request):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    items = CARTS.get(user, [])
    subtotal = sum(i["price"] * i["qty"] for i in items)
    return render("checkout.html", request, items=items, subtotal=round(subtotal, 2),
                  discount=0, total=round(subtotal, 2), coupon_msg=None, user=user)


@app.post("/checkout/coupon", response_class=HTMLResponse)
async def apply_coupon(request: Request, code: str = Form(...)):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    items = CARTS.get(user, [])
    subtotal = sum(i["price"] * i["qty"] for i in items)
    code = code.strip().upper()

    if code in VALID_COUPONS:
        pct = VALID_COUPONS[code]
        discount = round(subtotal * pct / 100, 2)
        msg = f"Coupon {code} applied — {pct}% off"
    elif code in EXPIRED_COUPONS:
        discount = 0
        msg = f"Coupon {code} has expired"
    else:
        discount = 0
        msg = f"Invalid coupon code: {code}"

    return render("checkout.html", request, items=items, subtotal=round(subtotal, 2),
                  discount=discount, total=round(subtotal - discount, 2),
                  coupon_msg=msg, user=user)


@app.post("/checkout/place")
async def place_order(request: Request):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    items = CARTS.get(user, [])
    if not items:
        return RedirectResponse("/cart")
    subtotal = sum(i["price"] * i["qty"] for i in items)
    order = {
        "id": str(uuid.uuid4())[:8].upper(),
        "products": list(items),
        "total": round(subtotal, 2),
        "placed_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    ORDERS.setdefault(user, []).insert(0, order)
    CARTS[user] = []
    return RedirectResponse("/orders", status_code=302)


# ---------- ORDERS ----------
@app.get("/orders", response_class=HTMLResponse)
async def orders(request: Request):
    user = get_session(request)
    if not user:
        return RedirectResponse("/login")
    user_orders = ORDERS.get(user, [])
    return render("orders.html", request, orders=user_orders, user=user)