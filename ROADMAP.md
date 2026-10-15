# Roadmap

## Implemented (MVP)

- Streamlit app scaffold (`platform/app.py`): sidebar navigation, Home dashboard, placeholder pages for
  10 modules, Paper Trading and Strategy Builder.
- Local single-user progress storage (`platform/progress/storage.py`): XP, daily streak, completed modules,
  validation, atomic JSON writes to `~/.quantacademy/progress.json`.
- "Mark module complete" button (+100 XP, once per module).
- Four basic achievements: First Steps, Halfway There, Quant Graduate, Consistent (7-day streak).
- `scripts/download_data.py`: writes synthetic sample market/news CSVs.

## Planned

### Core platform
- Lesson viewer with Jupyter notebook integration
- Code editor with an execution sandbox
- Local user authentication
- Database-backed storage for multiple users
- Automated tests (pytest) and CI
- Docker / docker-compose setup

### Curriculum
- Lesson content for the 10 modules outlined in the README (49 lessons), under `curriculum/`
- Exercises with an autograder (`grading/`), quizzes with randomization
- Real historical market data instead of the synthetic samples

### Sandbox
- Paper trading simulator
- Strategy builder UI
- Backtesting environment
- LLM Lab with API integration (keys via `.env`)

### Gamification & community
- More achievements (quiz, project and trading milestones), extended XP rules
- Leaderboards, discussion forums, peer review, completion certificates

### Polish
- Performance optimization, mobile responsiveness, documentation, public launch
