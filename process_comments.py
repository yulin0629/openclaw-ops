import os
import requests
import json

token = os.getenv("GITHUB_TOKEN")
repo = "yulin0629/openclaw-ops"

tasks = [
    {"cid": "3143995718", "tid": "PRRT_kwDORnwoX859rm5c", "reply": "True. The doc mixed string and boolean forms for channel-level blockStreaming. I standardized the channel override wording to boolean true/false to match the later examples and agent_runtime references in 2bb9a86."},
    {"cid": "3143995737", "tid": "PRRT_kwDORnwoX859rm5o", "reply": "Partly true: the loader does not require the folder name to match the SKILL name, but the example was unnecessarily confusing. I aligned the example to my_skill in 2bb9a86 to avoid ambiguity."},
    {"cid": "3143995748", "tid": "PRRT_kwDORnwoX859rm5v", "reply": "True. That fenced block was labeled as JSON but was not valid standalone JSON. I wrapped it as a complete JSON object in 2bb9a86."},
    {"cid": "3143995767", "tid": "PRRT_kwDORnwoX859rm59", "reply": "True. Same issue here: the snippet was not valid standalone JSON as written. I wrapped it as a complete JSON object in 2bb9a86."},
    {"cid": "3143995784", "tid": "PRRT_kwDORnwoX859rm6J", "reply": "True. The profile type list was missing the extension-relay mode that is documented later in the file. I added it to the list in 2bb9a86."},
    {"cid": "3143995796", "tid": "PRRT_kwDORnwoX859rm6R", "reply": "True. The retry narrative and config example disagreed. I aligned the config example with the documented 30s / 1m / 5m backoff sequence in 2bb9a86."},
    {"cid": "3143995807", "tid": "PRRT_kwDORnwoX859rm6d", "reply": "True. plugins.md and security.md were describing different security behavior. I updated plugins.md to match the security warning that lifecycle scripts may execute during dependency installation in 2bb9a86."}
]

def add_reply(tid, body):
    query = """
    mutation($id: ID!, $body: String!) {
      addPullRequestReviewThreadReply(input: {pullRequestReviewThreadId: $id, body: $body}) {
        comment {
          id
        }
      }
    }
    """
    variables = {"id": tid, "body": body}
    resp = requests.post("https://api.github.com/graphql",
                         headers={"Authorization": f"bearer {token}"},
                         json={"query": query, "variables": variables})
    return resp

def resolve_thread(tid):
    query = """
    mutation($id: ID!) {
      resolveReviewThread(input: {threadId: $id}) {
        thread {
          isResolved
        }
      }
    }
    """
    variables = {"id": tid}
    resp = requests.post("https://api.github.com/graphql",
                         headers={"Authorization": f"bearer {token}"},
                         json={"query": query, "variables": variables})
    return resp

for t in tasks:
    # Reply using GraphQL
    r_resp = add_reply(t['tid'], t['reply'])
    r_data = r_resp.json()
    if r_resp.status_code == 200 and "errors" not in r_data:
        r_status = "Success"
    else:
        r_status = f"Failed ({r_resp.status_code}: {json.dumps(r_data.get('errors', ''))[:100]})"
    
    # Resolve
    res_resp = resolve_thread(t['tid'])
    res_data = res_resp.json()
    if res_resp.status_code == 200 and "errors" not in res_data:
        res_status = "Success"
    else:
        res_status = f"Failed ({res_resp.status_code}: {json.dumps(res_data.get('errors', ''))[:100]})"
        
    print(f"Thread {t['tid']}: Reply {r_status}, Resolve {res_status}")
