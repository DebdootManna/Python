import requests

# Tokens and usernames
GITHUB_TOKEN = "your_github_token"
GITLAB_TOKEN = "your_gitlab_token"
GITHUB_USERNAME = "DebdootManna"
GITLAB_USERNAME = "debdootmanna007"  # usually GitLab username

# GitHub API headers
gh_headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# GitLab API headers
gl_headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}

# Fetch all GitHub repos
repos = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100&type=owner", headers=gh_headers).json()

for repo in repos:
    repo_name = repo["name"]
    clone_url = repo["clone_url"]

    print(f"\n🔁 Syncing repo: {repo_name}")

    # 1. Create repo on GitLab
    gl_repo_url = f"https://gitlab.com/api/v4/projects"
    gl_data = {
        "name": repo_name,
        "namespace_id": None,  # optional: set namespace if using groups
        "visibility": "private"
    }
    gl_create = requests.post(gl_repo_url, headers=gl_headers, data=gl_data)

    if gl_create.status_code == 201:
        print(f"✅ Created GitLab repo: {repo_name}")
        gitlab_project_id = gl_create.json()["id"]

        # 2. Enable pull mirroring
        mirror_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{repo_name}.git"

        mirror_data = {
            "import_url": mirror_url
        }

        mirror_api = f"https://gitlab.com/api/v4/projects/{gitlab_project_id}/mirror/pull"
        mirror_resp = requests.post(mirror_api, headers=gl_headers, data=mirror_data)

        if mirror_resp.status_code in [200, 201]:
            print(f"🔄 Mirroring enabled for {repo_name}")
        else:
            print(f"⚠️ Mirror failed: {mirror_resp.text}")
    else:
        print(f"⚠️ GitLab repo creation failed: {gl_create.text}")
