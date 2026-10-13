\# Bug Report — Remove Item Button Not Working



\---



\## Defect Title



\*\*Remove Item button on Cart page does not respond — item remains in cart and subtotal does not update\*\*



\---



\## Summary



On the Shopping Cart page, clicking the \*\*Remove\*\* button next to a product has no effect. The item stays in the cart, the item count remains unchanged, and the subtotal is not recalculated.



\---



\## Environment



| Field | Value |

|-------|-------|

| \*\*Application\*\* | ShopQA (http://localhost:8000) |

| \*\*Browser\*\* | Google Chrome 130 (Windows 11) |

| \*\*Build\*\* | v1.0 |

| \*\*Test Type\*\* | Manual / Functional |

| \*\*Reported By\*\* | Venkat Bandi |

| \*\*Reported On\*\* | 2026-10-13 |



\---



\## Pre-conditions



1\. User is registered and logged in

2\. At least one product is present in the shopping cart



\---



\## Steps to Reproduce



1\. Log in to ShopQA with valid credentials (`testuser@shop.com` / `Test@123`)

2\. Search for any product (e.g., \*\*iPhone 15 Pro\*\*)

3\. Add the product to the cart with quantity \*\*1\*\*

4\. Navigate to the \*\*Cart\*\* page (`/cart`)

5\. Click the \*\*Remove\*\* button next to the product

6\. Observe the cart contents and subtotal



\---



\## Expected Result



\- The selected product is removed from the cart

\- The cart item count decreases by 1

\- The subtotal is recalculated and updated immediately

\- If the cart becomes empty, a "Your cart is empty" message is shown



\---



\## Actual Result



\- \*\*No response\*\* when the Remove button is clicked

\- The product remains in the cart

\- Cart item count does not change

\- Subtotal remains the same



\*\*Evidence:\*\* Screenshot attached at `reports/screenshots/`



\---



\## Severity \& Priority



| Classification | Value | Justification |

|----------------|-------|---------------|

| \*\*Severity\*\* | \*\*High\*\* | Blocks a core cart management function. Users cannot remove unwanted items, forcing them to abandon the cart or place incorrect orders. |

| \*\*Priority\*\* | \*\*High\*\* | Affects 100% of users attempting to remove items. Must be fixed before release; critical for checkout flow integrity. |



\---



\## Impact



\- \*\*User Impact:\*\* Cannot correct cart contents — frustration, drop-off, incorrect orders

\- \*\*Business Impact:\*\* Lost revenue from abandoned carts; increased support tickets

\- \*\*Data Impact:\*\* Cart totals become inaccurate if other operations rely on the state



\---



\## Possible Cause (Suggestion)



Backend route `POST /cart/remove/{pid}` in `app/main.py` currently returns a `302` redirect \*\*without performing any removal logic\*\*. Cart state is not mutated in the in-memory store.



```python

@app.post("/cart/remove/{pid}")

async def remove\_from\_cart(request: Request, pid: int):

&#x20;   # 🐛 DELIBERATE BUG: does nothing — item stays in cart

&#x20;   return RedirectResponse("/cart", status\_code=302)

