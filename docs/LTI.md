# LTI

ObzueAI Professor is not yet a campus launch tool. This is the integration a university will ask for. LTI 1.3 is the current standard. LTI Advantage is three optional services on top of it, not a second standard.

## What the campus system must be given

- Launch URL
- Login URL, also called the OIDC login URL
- Redirect URIs
- Public key or a JWKS URL
- A separate deep-linking URL if teachers pick a lesson from inside the campus editor

Canvas, Moodle, Brightspace, Blackboard, and Open edX can all be the platform. Each deployment turns services on or off. Supporting a service does not mean a given campus has granted it.

## The launch

1. The learner opens the activity in the campus system.
2. The platform sends the browser to the login URL with an issuer, a client id, and a login hint.
3. Professor redirects back to the platform's authentication URL with a one-time state and nonce.
4. The platform returns an `id_token`. Professor checks the signature against the platform's keys, then checks issuer, audience, expiry, nonce, and deployment id.
5. The session opens on the lesson that was linked. It does not open the rest of the campus.

## Advantage services

| Service | What it does |
|---|---|
| Deep Linking | A teacher chooses the lesson while building the course, and the campus stores that link. |
| Names and Role Provisioning | Professor can read the roster for that course when the campus allows it. |
| Assignment and Grade Services | A score can be written to one gradebook column. Declarative mode uses the column the campus created. Programmatic mode lets the tool manage its own columns. |

Grades are the reason a department pays. A claim or a review score should be able to post back. Until the keypair, the login URL, and the launch URL exist, do not tell a campus that this is connected.
