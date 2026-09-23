"""Minimal TypeSafe demo: judge a support ticket with Noul, Choice, and Score.

Requires TYPESAFE_API_KEY in the environment or a local .env file (get a key
at https://console.typesafe.ai/keys). Install deps with:
    pip install -r requirements.txt
"""

from dotenv import load_dotenv
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

load_dotenv()

TICKET = (
    "Hi, I've been trying to connect my Stripe account for two days now "
    "and it keeps failing. This is blocking payouts to my customers and "
    "I need this fixed today."
)


def main() -> None:
    with TypeSafeClient() as client:
        result = client.system_one(
            state=TICKET,
            questions={
                "is_billing": Noul(
                    instructions="Is this ticket about billing or payments?",
                ),
                "team": Choice(
                    instructions="Which team should handle this ticket?",
                    criteria={
                        "billing": "Payments, invoicing, refunds",
                        "technical": "Bugs, outages, integrations",
                        "sales": "Pricing, upgrades, new accounts",
                    },
                ),
                "urgency": Score(
                    instructions="How urgent is this ticket?",
                    criteria=["Low", "Medium", "High"],
                ),
            },
        )

    print(f"Is billing-related : {result.nouls['is_billing'].noul:.2f}")
    print(f"Route to team       : {result.choices['team'].choice}")
    print(f"Urgency             : {result.scores['urgency'].score}")


if __name__ == "__main__":
    main()
