// Replace if using a different env file or config
require("dotenv").config({ path: "./.env" });
const express = require("express");
const app = express();
const { resolve } = require("path");
const bodyParser = require("body-parser");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

app.use(express.static(process.env.STATIC_DIR));
// Use JSON parser for all non-webhook routes
app.use((request, response, next) => {
  if (request.originalUrl === "/webhook") {
    next();
  } else {
    bodyParser.json()(request, response, next);
  }
});

app.get("/", (request, response) => {
  const path = resolve(process.env.STATIC_DIR + "/index.html");
  response.sendFile(path);
});

app.get("/success", (request, response) => {
  const path = resolve(process.env.STATIC_DIR + "/success.html");
  response.sendFile(path);
});

app.post("/create-checkout-session", async (request, response) => {
  const session = await stripe.checkout.sessions.create({
    success_url: "http://localhost:4242/success?id={CHECKOUT_SESSION_ID}",
    cancel_url: "http://localhost:4242/cancel",
    payment_method_types: ["card"],
    mode: "payment",
    line_items: [{
      price: "price_1I78l4GBXWEcKDMylfxHVhTJ",
      quantity: request.body.quantity,
    }] 
  });
  response.json({
    id: session.id,
  })
});

// Stripe requires the raw body to construct the event
app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, webhookSecret);
    } catch (err) {
      // On error, log and return the error message
      console.log(`❌ Error message: ${err.message}`);
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Successfully constructed event
    console.log("✅ Success:", event.id);

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  }
);

app.listen(4242, () => console.log(`Node server listening on port ${4242}!`));
