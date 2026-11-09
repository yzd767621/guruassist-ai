# GuruAssist — FOI 2026 Agentic AI Challenge Submission Package
## 1. Participant & Project Details (Ready to Copy-Paste)

* **Challenge:** Festival Idea Putrajaya (FOI) 2026 — Agentic AI Challenge (Theme: *Edutainment & Innovation*)
* **Category (Kategori):** **Kategori IPT**
* **Name:** **YEOH ZHENG DA**
* **Institution:** **Universiti Teknologi Malaysia (UTM)** — Bachelor of Artificial Intelligence
* **Email:** `zhengdayeoh120@gmail.com` | **Phone:** `+60 18-201 4893`
* **Project Title:** **GuruAssist — Autonomous AI Agent for PBD (Pentaksiran Bilik Darjah) Paperwork & Remedial Planning**

---

## 2. Executive Summary / Abstrak Projek (EN & BM)

### English Version:
Malaysian school teachers spend hours every week manually compiling **Pentaksiran Bilik Darjah (PBD)** records, checking score sheets for missing or mistyped marks, determining **Tahap Penguasaan (TP1–TP6)** levels, writing daily remedial lesson plans (**Rancangan Pengajaran Harian / RPH**), and drafting bilingual progress updates for parents—taking valuable time away from actual classroom teaching.

**GuruAssist** is an autonomous, tool-using AI agent powered by **Google Gemini 2.5 Flash function-calling**. Unlike a passive Q&A chatbot, the teacher simply provides a single high-level goal (e.g., *"Process PBD for Class 5 Bestari and prepare remedial plans"*) along with a CSV or photo of a score sheet. **GuruAssist** autonomously plans and executes a multi-step tool loop:
1. **`load_class_data` & `extract_scores_from_image`:** Parses raw student score tables or OCRs photographed mark sheets.
2. **`validate_scores` & `flag_issue`:** Autonomously detects data anomalies (such as missing scores or impossible typos like `200/20`) and flags them for teacher review (`needs_teacher` / `exclude`) rather than hallucinating numbers.
3. **`compute_tp_levels`:** Deterministically computes total marks, percentages, and TP1–TP6 levels based on teacher-adjustable thresholds.
4. **`analyse_class_weakness`:** Identifies class-wide skill bottlenecks (e.g., detecting that 10 out of 12 students scored below 50% in *Pembahagian Pecahan / Division of Fractions*).
5. **`draft_rph` & `draft_parent_report`:** Autonomously generates a targeted 60-minute remedial RPH lesson plan and personalized bilingual (Bahasa Melayu & English) parent progress reports, ready for one-click CSV/TXT export.

### Versi Bahasa Melayu:
Guru-guru di Malaysia menghabiskan berjam-jam setiap minggu untuk menguruskan kerja perkeranian **Pentaksiran Bilik Darjah (PBD)**—termasuk menyemak ralat markah, menentukan **Tahap Penguasaan (TP1–TP6)**, menyediakan **Rancangan Pengajaran Harian (RPH)** pemulihan, dan menulis laporan kemajuan dwibahasa kepada ibu bapa.

**GuruAssist** ialah ejen AI autonomi berasaskan panggilan fungsi (**Function Calling**) **Google Gemini 2.5 Flash**. Berbeza daripada chatbot soal jawab biasa, guru hanya perlu memberikan satu matlamat utama dan memuat naik jadual markah (CSV atau gambar). **GuruAssist** merancang langkahnya sendiri secara autonomi dan memanggil 8 alat khusus untuk mengesan markah hilang atau ralat kemasukan (seperti `200/20`), mengira tahap TP1–TP6 secara tepat, mengenal pasti kemahiran paling lemah seluruh kelas (*Pembahagian Pecahan*), mendraf RPH pemulihan 60 minit, serta menyediakan laporan kemajuan ibu bapa dalam Bahasa Melayu dan Bahasa Inggeris. Guru kekal mempunyai kuasa semakan terakhir (*Human-in-the-Loop*).

---

## 3. Truthful Declaration of AI Models, Frameworks & Tools (Senarai Pengisytiharan Alat AI)

| Category | Declared Tool / Model | Exact Role in GuruAssist |
| :--- | :--- | :--- |
| **Foundation AI Model** | **Google Gemini 2.5 Flash** (`generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent`) | Executes multi-turn autonomous reasoning, native tool/function calling (`functionDeclarations` / `functionCall` / `functionResponse`), Vision OCR for photographed score sheets, RPH drafting, and bilingual (BM/EN) parent report generation. |
| **Agent Architecture** | **Custom ReAct Tool-Calling Loop (Vanilla JavaScript)** + **Deterministic Rule-Based Offline Fallback Planner** | Implements stateful multi-step tool execution (`load_class_data`, `validate_scores`, `flag_issue`, `compute_tp_levels`, `analyse_class_weakness`, `draft_rph`, `draft_parent_report`) with deterministic math calculation in JS so the LLM never hallucinates arithmetic. |
| **Frontend & Export** | **HTML5 / CSS3 / Vanilla ES6 JavaScript** | Single-file zero-dependency web application with mandatory `DEMO / SAMPLE` watermarks and client-side CSV/TXT export. |
| **Development Assistance** | **Google Gemini & Anthropic Claude** | Used as coding assistants during hackathon development. |

---

## 4. 3-Minute Demo Video Script (With Bahasa Melayu Subtitles)

* **0:00 – 0:25 | The Real Problem:**
  * *Action:* Show `GuruAssist` screen with the top `DEMO / SAMPLE` banner visible.
  * *Voiceover:* "Hi judges! Malaysian teachers are overwhelmed by PBD (Pentaksiran Bilik Darjah) paperwork—checking mark sheets, calculating TP1 to TP6 levels, writing remedial RPH lesson plans, and messaging parents. **GuruAssist** is an autonomous AI agent powered by **Google Gemini 2.5 Flash function-calling** that completes this entire workflow from a single goal."
  * *BM Subtitle:* *Guru-guru di Malaysia dibebani kerja perkeranian PBD. GuruAssist ialah ejen AI autonomi berasaskan Google Gemini 2.5 Flash yang menyelesaikan keseluruhan aliran kerja PBD ini daripada satu arahan matlamat sahaja.*

* **0:25 – 1:40 | Live Autonomous Gemini Function-Calling Run:**
  * *Action:* Paste your Gemini API Key in the left box, show the loaded `5 Bestari` sample class (12 students), and click **`▶ Run Autonomous Agent`**. Point to the Center Column as real Gemini API steps stream in!
  * *Voiceover:* "We paste our live Gemini API key, load Class 5 Bestari's Mathematics scores, and click Run Agent. Watch the live trace in the center panel: Gemini autonomously plans its workflow and calls `load_class_data` and `validate_scores`. Without any human prompting, it discovers two planted data anomalies: **Nurul Aina is missing a score on Question 3**, and **Amirul Hakimi has a typo of 200 out of 20 on Question 2**! The agent calls `flag_issue` to exclude the typo and mark the missing score for teacher verification, then calls `compute_tp_levels` and `analyse_class_weakness`—discovering that **Question 4 (Division of Fractions)** has a class average of only 32%!"
  * *BM Subtitle:* *Kita masukkan kunci API Gemini dan klik Run Agent. Ejen merancang langkahnya sendiri dan memanggil alat semakan data. Ia mengesan dua ralat secara autonomi: markah Nurul Aina yang kosong pada Soalan 3, dan ralat menaip 200/20 bagi Amirul Hakimi! Ejen menandakan ralat tersebut, mengira tahap TP1–TP6, dan mengesan bahawa Soalan 4 (Pembahagian Pecahan) ialah kelemahan utama kelas dengan purata hanya 32%!*

* **1:40 – 2:40 | Reviewing the 4 Teacher Deliverables & Offline Fallback:**
  * *Action:* Click through the 4 tabs on the Right Column (`PBD Table`, `Class Insights`, `Remedial RPH Draft`, `Parent Reports BM/EN`), and click **`⬇ Download PBD CSV`** and **`⬇ Download RPH & Reports (.txt)`**.
  * *Voiceover:* "In the right panel, all four teacher deliverables are ready: first, the complete **PBD Table** with TP badges and audit notes; second, **Class Insights** highlighting the 10 students who need help in Fraction Division; third, a tailored 60-minute **Remedial RPH Lesson Plan** using the Keep-Change-Flip method; and fourth, personalized **Bilingual Bahasa Melayu and English Parent Reports**! Teachers can download the CSV and RPH with one click, and if internet or API access is unavailable, GuruAssist transparently switches to its built-in deterministic offline rule mode. Thank you!"
  * *BM Subtitle:* *Di panel kanan, keempat-empat dokumen guru telah siap: Jadual PBD lengkap dengan tahap TP, Analisis Kelemahan Kelas, Draf RPH Pemulihan 60 minit, serta Laporan Kemajuan Ibu Bapa dwibahasa (BM & EN) yang boleh dimuat turun serta-merta. Terima kasih!*
