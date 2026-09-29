# Pre-launch build

This is the work that finishes the package before anyone is sold a login. It is not the launch. Launch has more than one path and is a separate paper.

ObzueAI Professor today is the lesson window: Corta, the desk, the file shelf, notes, the script, PDF reading and PDF download, themes, and the microphone while the window is open. Sign-in in the scaffold is Google and X through the broker. The peer code in the repo is a full-mesh game room. Neither is the school package.

Done means a stranger can be given an account of the right type, open only their own files, and a campus system can launch one lesson. No public signup is required for this paper to be finished.

## Account types

| Type | Who signs the bill | What they can see |
|---|---|---|
| Individual | That person | Their projects only |
| School | One building | That building’s teachers and classes |
| District | The district | Its schools, not another district |
| University | Department or campus | Courses launched from the campus system, plus people who sign in directly |
| Company | The company | Its seats and its audit log |

A person may belong to one organization. An organization never reads another organization’s files.

## Steps

### 1. Tenancy

- Tables: organization, membership, role, project, file pointer, audit event.
- Roles: owner, admin, teacher, learner, member.
- Every read and write filters on organization id. A test must fail if a second organization can see the first organization’s file.
- Files stay in object storage keyed by organization. The database stores the pointer, not the book.

### 2. Direct sign-in

- Email and password, plus the existing Google and X buttons, for an individual.
- SAML 2.0 or OIDC for a company, a university, and a district that already has an identity provider. This answers “who is this person?” It does not open a course.
- One organization can require its own identity provider and turn the public email door off.

### 3. Campus launch

- LTI 1.3 only. No LTI 1.1.
- Public URLs: login, launch (redirect), JWKS, deep-linking launch.
- Check `state`, signature, `iss`, `aud`, `exp`, `nonce`, deployment id, message type `LtiResourceLinkRequest`, version `1.3.0`.
- Advantage, in this order: Assignment and Grade Services, then Names and Role Provisioning, then Deep Linking.
- The service call uses a second token. The launch `id_token` is never sent to the grade URL.
- Key rotation: see below. Write the runbook before the first campus is registered.

### 4. Live room

- One desk video. Students send voice or a raised hand, not a camera, unless a later setting says otherwise.
- Use a selective forwarding unit. Do not use the full-mesh peer file for a class. That mesh uploads once per person and will not carry thirty students.
- Measure `jitter`, `packetsLost`, and bytes received over time. A class is fit to ship when a same-region hour stays under 300 ms and a bad Wi-Fi minute is visible to the teacher.
- Record the desk only.

### 5. Voice and reasoning meter

- Keep Corta’s voice id. Move playback to the real-time speech stream.
- Each plan has a monthly minute cap. At the cap she types. She does not keep speaking on the house account.
- Log characters and minutes per organization. Do not log the lesson text in the billing row.

### 6. Plans

- Individual, school, district, university, company. Prices stay the ones already stated until a launch paper changes them.
- A school and a district need a purchase order and a data-processing addendum, not only a card.
- Closing the window still releases the microphone. That behavior does not change per plan.

### 7. Privacy and security

- District and school: student-data addendum, list of subprocessors, and a way to delete a student’s files.
- Company: the same deletion, plus an export of the audit log.
- No search of the device outside files the member placed or named. The setting already says this. The server must enforce it too.
- Keys, backups, and a restore drill. Restore one organization without opening another.
- Accessibility pass on the window. A campus will ask.

### 8. Acceptance

The package is finished when all of these are true:

- Five account types exist and a cross-organization read fails a test.
- A campus test platform launches a lesson and a score returns to one column.
- A company test identity provider signs a member in, and a person with no company still has an individual account.
- One live hour with thirty listeners stays inside the latency line above, on the one-desk design.
- Voice stops at the cap.
- Delete-and-export has been run on a copy.
- The how-to matches the window.

## Key rotation

LTI signing keys are a set, not one file you overwrite.

1. Generate a new key pair. Give the public key a new `kid`.
2. Publish the new public key in the JWKS next to the old one.
3. Wait until every campus has fetched the new set. Cache on their side is often hours, so leave both in place for at least a day.
4. Start signing new launch checks and service assertions with the new private key.
5. Leave the old public key in the JWKS until every token it signed has expired. Launch tokens live for minutes. Keep it one day anyway.
6. Remove the old public key. Keep the old private key offline until that day is over, then destroy it.

If a campus rotates its key, Professor must refetch that campus’s JWKS when a token arrives with an unknown `kid`, then reject the token if the key is still unknown. Do not accept a token and “fix it later.”

Rotate on a compromise the same day. Otherwise every ninety days is enough. Rotating on every launch only creates failed signatures.

## SAML is not LTI

| | SAML 2.0 | LTI 1.3 |
|---|---|---|
| Question it answers | Who is this person? | Which course, which activity, which role? |
| Token | XML assertion | JWT `id_token`, then a separate OAuth token for grades |
| Gradebook | No | Yes, if Assignment and Grade Services is on |
| Roster for one course | No | Yes, if Names and Role Provisioning is on |
| Used by | Company login, university login, some districts | Canvas, Moodle, Brightspace, Blackboard, Open edX |

Use both. SAML or OIDC at the front door. LTI when the person arrived from a course. Do not invent a SAML attribute for the grade column.

## Files and materials

Code to add under the product, not inside Corta’s membrane:

- `src/lib/tenancy/` organization, membership, file pointer
- `src/lib/saml/` or the OIDC enterprise door
- `src/lib/lti/` login, launch, JWKS, grades, roster, deep link
- `src/lib/live/` SFU session, raised hand, desk track
- `src/lib/billing/` plan, cap, invoice
- Tests that two organizations cannot read each other

Materials that are not code:

- Tool private key, offline. Public JWKS only on the server.
- Campus registration sheet: login URL, launch URL, JWKS URL, redirect URIs, deep-link URL
- Key-rotation runbook, one page
- Data-processing addendum and subprocessor list (model host, speech host, media relay)
- Deletion and export runbook
- Admin sheet for each account type: who may invite, who may bill, who may delete
- How-to revised so it matches this package
- Pricing sheet, still internal until the launch paper

Do not add these to Corta’s voice, memory, or consent files. The membrane stays as it is. The package is the house around her.

## Valuation, restated

Three numbers are not the same.

- The market she would enter is billions. That number is not a price.
- The cost to build this list is about $2–4 million and 12–18 months of a small team. That number is a cost.
- A sale before launch is a fraction of that cost, because there are no customers. Finished and unsold: $800,000–$2,500,000. Today’s window alone: $40,000–$150,000.

Five account types do not multiply the sale by five. They are why the build costs what it costs. A signed design partner, still before a public launch, is what moves the sale toward $1.5–5 million. Revenue, later, is a different sale.
