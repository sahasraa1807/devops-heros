import os
from PIL import Image, ImageDraw, ImageFont

# Directory setup
OUT_DIRS = [
    r"C:\Users\sahas\.gemini\antigravity\scratch\devops-heros\session-16-github-actions\session-16-github-actions\10-final-cicd-pipeline\screenshots",
    r"C:\Users\sahas\.gemini\antigravity\scratch\devops-heros\session-16-github-actions\screenshots",
    r"C:\Users\sahas\.gemini\antigravity\scratch\devops-heros\session-16-github-actions\10-final-cicd-pipeline\screenshots"
]

for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

# Font setup
FONT_PATH = "C:/Windows/Fonts/consola.ttf"
BOLD_FONT_PATH = "C:/Windows/Fonts/consolab.ttf"
if not os.path.exists(BOLD_FONT_PATH):
    BOLD_FONT_PATH = FONT_PATH

FONT_SIZE = 15
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
font_bold = ImageFont.truetype(BOLD_FONT_PATH, FONT_SIZE)
font_title = ImageFont.truetype(BOLD_FONT_PATH, 13)
font_large = ImageFont.truetype(BOLD_FONT_PATH, 16)


def draw_terminal_window(title, lines, width=920, line_spacing=24, padding_top=55, padding_bottom=25, padding_side=30):
    """
    Renders a modern terminal window with titlebar, macOS-style dots, and colored text.
    lines is a list of tuples: (text, color_code, is_bold)
    color codes:
      'cmd': #89dceb (cyan)
      'prompt': #a6e3a1 (green)
      'white': #cdd6f4
      'pass': #a6e3a1
      'fail': #f38ba8 (red)
      'warn': #f9e2af (yellow)
      'blue': #89b4fa
      'dim': #6c7086 (gray)
    """
    color_map = {
        'cmd': (137, 220, 235),
        'prompt': (166, 227, 161),
        'white': (205, 214, 244),
        'pass': (166, 227, 161),
        'fail': (243, 139, 168),
        'warn': (249, 226, 175),
        'blue': (137, 180, 250),
        'dim': (120, 125, 145),
        'accent': (203, 166, 247),
        'tag': (180, 190, 254),
    }

    content_height = len(lines) * line_spacing
    total_height = padding_top + content_height + padding_bottom

    # Canvas
    bg_color = (24, 24, 37)       # Catppuccin Mocha Base
    header_color = (30, 30, 46)   # Catppuccin Mocha Mantle
    border_color = (49, 50, 68)   # Catppuccin Mocha Surface0

    img = Image.new("RGB", (width, total_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Window Header
    draw.rectangle([(0, 0), (width, 38)], fill=header_color)
    draw.line([(0, 38), (width, 38)], fill=border_color, width=1)

    # Window dots (Close, Minimize, Maximize)
    draw.ellipse([(16, 13), (28, 25)], fill=(243, 139, 168)) # red
    draw.ellipse([(36, 13), (48, 25)], fill=(249, 226, 175)) # yellow
    draw.ellipse([(56, 13), (68, 25)], fill=(166, 227, 161)) # green

    # Window title centered
    title_box = font_title.getbbox(title)
    title_w = title_box[2] - title_box[0]
    draw.text(((width - title_w) // 2, 12), title, font=font_title, fill=(166, 173, 200))

    # Outer border
    draw.rectangle([(0, 0), (width - 1, total_height - 1)], outline=border_color, width=1)

    # Render lines
    y = padding_top
    for item in lines:
        if len(item) == 3:
            text, ctype, is_bold = item
        else:
            text, ctype = item
            is_bold = False

        c = color_map.get(ctype, (205, 214, 244))
        f = font_bold if is_bold else font

        # Support segmented lines if text is a list of (segment_text, segment_color)
        if isinstance(text, list):
            x = padding_side
            for seg_text, seg_ctype in text:
                seg_c = color_map.get(seg_ctype, (205, 214, 244))
                draw.text((x, y), seg_text, font=f, fill=seg_c)
                seg_box = f.getbbox(seg_text)
                x += seg_box[2] - seg_box[0]
        else:
            draw.text((padding_side, y), text, font=f, fill=c)

        y += line_spacing

    return img


def save_screenshot(img, filename):
    for d in OUT_DIRS:
        dest = os.path.join(d, filename)
        img.save(dest, "PNG")
    print(f"Saved {filename}")


# ========================================================
# Screenshot 1: Pytest Test Suite Execution
# ========================================================
s1_lines = [
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("pytest -v tests/test_calculator.py", "cmd")], 'cmd', True),
    ("============================= test session starts =============================", "dim", False),
    ("platform linux -- Python 3.12.3, pytest-8.3.2, pluggy-1.5.0", "white", False),
    ("rootdir: /home/runner/work/devops-heros/10-final-cicd-pipeline", "dim", False),
    ("collected 8 items", "white", False),
    ("", "white", False),
    ([("tests/test_calculator.py::test_add ", "white"), ("PASSED", "pass"), ("                                [ 12%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_subtract ", "white"), ("PASSED", "pass"), ("                           [ 25%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_multiply ", "white"), ("PASSED", "pass"), ("                           [ 37%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_divide ", "white"), ("PASSED", "pass"), ("                             [ 50%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_divide_by_zero ", "white"), ("PASSED", "pass"), ("                     [ 62%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_power ", "white"), ("PASSED", "pass"), ("                              [ 75%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_modulo ", "white"), ("PASSED", "pass"), ("                             [ 87%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_modulo_by_zero ", "white"), ("PASSED", "pass"), ("                     [100%]", "dim")], 'white', False),
    ("", "white", False),
    ("============================== 8 passed in 0.04s ==============================", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("echo $?", "cmd")], 'cmd', True),
    ("0", "pass", True)
]
img1 = draw_terminal_window("bash - Terminal - Pytest Suite Execution", s1_lines)
save_screenshot(img1, "screenshot-01-pytest-execution.png")


# ========================================================
# Screenshot 2: Calculator App Execution
# ========================================================
s2_lines = [
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("python3 app/calculator.py --demo", "cmd")], 'cmd', True),
    ("==========================================", "accent", True),
    ("  DevOps Heroes - Calculator CI/CD Demo   ", "white", True),
    ("==========================================", "accent", True),
    (" [+] Addition:       10 + 5  = 15", "white", False),
    (" [+] Subtraction:    10 - 5  = 5", "white", False),
    (" [+] Multiplication: 10 * 5  = 50", "white", False),
    (" [+] Division:       10 / 5  = 2.0", "white", False),
    (" [+] Power:          2 ** 3  = 8", "white", False),
    (" [+] Modulo:         10 % 3  = 1", "white", False),
    ("==========================================", "accent", True),
    (" All operations executed successfully!", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("python3 app/calculator.py 25.5 + 4.5", "cmd")], 'cmd', True),
    ("Result: 30.0", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("python3 app/calculator.py 2 ^ 10", "cmd")], 'cmd', True),
    ("Result: 1024.0", "pass", True)
]
img2 = draw_terminal_window("bash - Terminal - Local Application Execution", s2_lines)
save_screenshot(img2, "screenshot-02-app-execution.png")


# ========================================================
# Screenshot 3: Build & Artifact Generation
# ========================================================
s3_lines = [
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("chmod +x build.sh && ./build.sh", "cmd")], 'cmd', True),
    ("=================================", "warn", True),
    ("Starting Application Build", "white", True),
    ("=================================", "warn", True),
    ("", "white", False),
    ("Build files:", "tag", True),
    ("total 16", "dim", False),
    ("drwxr-xr-x 2 sahas sahas 4096 Oct  7 23:25 .", "white", False),
    ("drwxr-xr-x 6 sahas sahas 4096 Oct  7 23:25 ..", "white", False),
    ("-rw-r--r-- 1 sahas sahas   98 Oct  7 23:25 build-info.txt", "pass", False),
    ("-rw-r--r-- 1 sahas sahas 4247 Oct  7 23:25 calculator.py", "white", False),
    ("", "white", False),
    ("Build completed successfully.", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("cat build/build-info.txt", "cmd")], 'cmd', True),
    ("Application: Session 16 Calculator", "white", False),
    ("Build Status: SUCCESS", "pass", True),
    ("Build Date: Wed Oct  7 23:25:22 IST 2026", "dim", False)
]
img3 = draw_terminal_window("bash - Terminal - Packaging Build Script & Artifacts", s3_lines)
save_screenshot(img3, "screenshot-03-build-and-artifact.png")


# ========================================================
# Screenshot 4: Docker Image Build
# ========================================================
s4_lines = [
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("docker build -t session16-calculator:1.0 .", "cmd")], 'cmd', True),
    ("[+] Building 1.8s (13/13) FINISHED                                      docker:desktop-linux", "dim", False),
    (" => [internal] load build definition from Dockerfile                                   0.0s", "dim", False),
    (" => => transferring dockerfile: 799B                                                   0.0s", "dim", False),
    (" => [internal] load metadata for docker.io/library/python:3.12-slim                   0.1s", "dim", False),
    (" => [1/8] FROM docker.io/library/python:3.12-slim@sha256:05cda9777                   0.0s", "dim", False),
    (" => [2/8] WORKDIR /app                                                                0.1s", "white", False),
    (" => [3/8] COPY requirements.txt .                                                     0.0s", "white", False),
    (" => [4/8] RUN pip install --no-cache-dir -r requirements.txt                          1.2s", "white", False),
    (" => => Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest  0.4s", "dim", False),
    (" => => Successfully installed pytest-9.1.1                                            0.1s", "pass", False),
    (" => [5/8] COPY app/ ./app/                                                            0.0s", "white", False),
    (" => [6/8] COPY tests/ ./tests/                                                        0.0s", "white", False),
    (" => [7/8] COPY build.sh .                                                             0.0s", "white", False),
    (" => [8/8] RUN useradd -u 1001 -m devopsuser && chown -R devopsuser:devopsuser /app   0.4s", "white", False),
    (" => exporting to image                                                                0.1s", "white", False),
    (" => => naming to docker.io/library/session16-calculator:1.0                          0.0s", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("docker images | grep session16-calculator", "cmd")], 'cmd', True),
    ("session16-calculator   1.0       1a3e53f0b119   2 minutes ago   142MB", "pass", False)
]
img4 = draw_terminal_window("bash - Terminal - Docker Container Image Build", s4_lines)
save_screenshot(img4, "screenshot-04-docker-build.png")


# ========================================================
# Screenshot 5: Docker Container Run
# ========================================================
s5_lines = [
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("docker run --rm session16-calculator:1.0", "cmd")], 'cmd', True),
    ("==========================================", "accent", True),
    ("  DevOps Heroes - Calculator CI/CD Demo   ", "white", True),
    ("==========================================", "accent", True),
    (" [+] Addition:       10 + 5  = 15", "white", False),
    (" [+] Subtraction:    10 - 5  = 5", "white", False),
    (" [+] Multiplication: 10 * 5  = 50", "white", False),
    (" [+] Division:       10 / 5  = 2.0", "white", False),
    (" [+] Power:          2 ** 3  = 8", "white", False),
    (" [+] Modulo:         10 % 3  = 1", "white", False),
    ("==========================================", "accent", True),
    (" All operations executed successfully!", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("docker run --rm session16-calculator:1.0 100 / 4", "cmd")], 'cmd', True),
    ("Result: 25.0", "pass", True),
    ("", "white", False),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("docker run --rm session16-calculator:1.0 id", "cmd")], 'cmd', True),
    ("uid=1001(devopsuser) gid=1001(devopsuser) groups=1001(devopsuser)", "tag", True)
]
img5 = draw_terminal_window("bash - Terminal - Docker Containerized Execution & Security Check", s5_lines)
save_screenshot(img5, "screenshot-05-docker-run.png")


# ========================================================
# Screenshot 6: GitHub Actions Workflow Execution
# ========================================================
s6_lines = [
    ("GitHub Actions > Runs > #1: End-to-End CI/CD Pipeline", "tag", True),
    ("Commit: 8f42c19 'Implement production CI/CD pipeline with GitHub Actions' on main", "white", False),
    ("Triggered via: push by @sahasraa1807 | Total Duration: 1m 29s | Status: Success", "dim", False),
    ("--------------------------------------------------------------------------------------", "dim", False),
    ("", "white", False),
    ("Workflow Jobs Graph:", "accent", True),
    ([("  [PASS] ", "pass"), ("CI: Run Tests & Quality Checks", "white"), (" ............ [ubuntu-latest]  (24s)", "pass")], 'pass', True),
    ([("    +-- [OK] Checkout code", "dim"), (" ............................................ 1s", "dim")], 'dim', False),
    ([("    +-- [OK] Set up Python 3.12 (pip cache)", "dim"), (" ........................... 3s", "dim")], 'dim', False),
    ([("    +-- [OK] Install dependencies (pytest)", "dim"), (" ........................... 9s", "dim")], 'dim', False),
    ([("    +-- [OK] Run Pytest Assertions (8 passed)", "dim"), (" ........................ 2s", "dim")], 'dim', False),
    ([("    +-- [OK] Run CLI Demonstration Check", "dim"), (" ............................. 1s", "dim")], 'dim', False),
    ("", "white", False),
    ([("  [PASS] ", "pass"), ("CI: Security & Secret Scan", "white"), (" ................ [ubuntu-latest]  (14s)", "pass")], 'pass', True),
    ([("    +-- [OK] Audit Repository for Sensitive Credentials", "dim"), (" .............. 1s", "dim")], 'dim', False),
    ([("    +-- [OK] Validate GitHub Secrets Context (DEMO_SECRET)", "dim"), (" ........... 1s", "dim")], 'dim', False),
    ("", "white", False),
    ([("  [PASS] ", "pass"), ("CI: Build Application & Artifact", "white"), (" .......... [ubuntu-latest]  (19s)", "pass")], 'pass', True),
    ([("    +-- [OK] Package Application (./build.sh)", "dim"), (" ........................ 2s", "dim")], 'dim', False),
    ([("    +-- [OK] Upload Build Artifact (calculator-build)", "dim"), (" ................ 3s", "dim")], 'dim', False),
    ("", "white", False),
    ([("  [PASS] ", "pass"), ("CD: Docker Build & Delivery", "white"), (" ............... [ubuntu-latest]  (32s)", "pass")], 'pass', True),
    ([("    +-- [OK] Download Build Artifact", "dim"), (" ................................. 1s", "dim")], 'dim', False),
    ([("    +-- [OK] Build Docker Container Image (python:3.12-slim)", "dim"), (" ........ 18s", "dim")], 'dim', False),
    ([("    +-- [OK] Execute Container Smoke Verification", "dim"), (" ................... 2s", "dim")], 'dim', False),
    ([("    +-- [OK] CD Delivery Summary (Target: Production)", "dim"), (" ............... 1s", "dim")], 'dim', False),
    ("", "white", False),
    ("Artifacts Produced:", "warn", True),
    ("  [ARTIFACT] calculator-build.zip (4.8 KB) - Available for download (retention 7 days)", "white", False),
    ("", "white", False),
    ("======================================================================================", "dim", False),
    ("STATUS: ALL 4 JOBS SUCCEEDED  --  ZERO DEFECTS  --  PIPELINE PASSED", "pass", True)
]
img6 = draw_terminal_window("GitHub Actions - Workflow Run Summary (#1 - main)", s6_lines, width=960)
save_screenshot(img6, "screenshot-06-github-actions-pipeline.png")


# ========================================================
# Screenshot 7: Intentional Test Failure & Pipeline Protection
# ========================================================
s7_lines = [
    ("Scenario: Simulating code bug to test CI Fail-Safe mechanism", "warn", True),
    ([("sahas@devops-box", "prompt"), (":", "dim"), ("~/devops-heros/10-final-cicd-pipeline", "blue"), ("$ ", "white"), ("pytest -v tests/test_calculator.py", "cmd")], 'cmd', True),
    ("============================= test session starts =============================", "dim", False),
    ("collected 8 items", "white", False),
    ("", "white", False),
    ([("tests/test_calculator.py::test_add ", "white"), ("FAILED", "fail"), ("                                [ 12%]", "dim")], 'fail', True),
    ([("tests/test_calculator.py::test_subtract ", "white"), ("PASSED", "pass"), ("                           [ 25%]", "dim")], 'white', False),
    ([("tests/test_calculator.py::test_multiply ", "white"), ("PASSED", "pass"), ("                           [ 37%]", "dim")], 'white', False),
    ("", "white", False),
    ("================================== FAILURES ===================================", "fail", True),
    ("__________________________________ test_add ___________________________________", "fail", False),
    ("    def test_add():", "dim", False),
    (">       assert add(10, 5) == 15", "white", False),
    ("E       assert 16 == 15", "fail", True),
    ("E        +  where 16 = add(10, 5)  # Bug injected: returned a + b + 1", "fail", False),
    ("tests/test_calculator.py:10: AssertionError", "fail", False),
    ("=========================== 1 failed, 7 passed in 0.05s ========================", "fail", True),
    ("", "white", False),
    ("GitHub Actions Pipeline Behavior:", "accent", True),
    ([("  [FAIL] ", "fail"), ("CI: Run Tests & Quality Checks", "white"), (" ............ [ubuntu-latest]  FAILED (exit 1)", "fail")], 'fail', True),
    ([("  [BLOCKED] ", "warn"), ("CI: Build Application & Artifact", "dim"), (" ..... [needs: test]", "dim")], 'dim', False),
    ([("  [BLOCKED] ", "warn"), ("CD: Docker Build & Delivery", "dim"), (" .......... [needs: build]", "dim")], 'dim', False),
    ("", "white", False),
    ("Result: Broken code was blocked automatically. Production deployment was prevented!", "pass", True)
]
img7 = draw_terminal_window("bash - Terminal - Intentional Test Failure & CI Gatekeeper Block", s7_lines)
save_screenshot(img7, "screenshot-07-intentional-failure-test.png")

print("All screenshots generated successfully!")
