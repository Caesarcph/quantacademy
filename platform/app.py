"""Streamlit entrypoint for QuantAcademy MVP UI."""

import streamlit as st

from platform.progress.storage import (
    DEFAULT_XP_PER_MODULE,
    Progress,
    complete_module,
    get_achievements,
    get_stats,
    load_progress,
    save_progress,
    touch_activity,
    validate_progress,
)


st.set_page_config(
    page_title="QuantAcademy",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


MODULES: list[str] = [
    "Module 1: Python Foundations",
    "Module 2: Technical Analysis",
    "Module 3: Statistical Analysis",
    "Module 4: Backtesting",
    "Module 5: Risk Management",
    "Module 6: Machine Learning",
    "Module 7: Deep Learning",
    "Module 8: NLP",
    "Module 9: LLM Trading",
    "Module 10: Multi-Agent Systems",
]


def _persist_progress(progress: Progress) -> Progress:
    """Save progress and sync session state in one place."""
    save_progress(progress)
    st.session_state.qa_progress = progress
    return progress


def _render_sidebar(progress: Progress) -> None:
    st.sidebar.title("🎓 QuantAcademy")

    st.sidebar.subheader("📊 Your Progress")
    st.sidebar.write(f"**Streak:** {progress.streak_days} day(s)")
    st.sidebar.write(f"**XP:** {progress.xp}")
    st.sidebar.write(f"**Completed modules:** {len(progress.completed_modules)}/{len(MODULES)}")

    with st.sidebar.expander("Completed", expanded=False):
        if progress.completed_modules:
            for m in progress.completed_modules:
                st.write(f"✅ {m}")
        else:
            st.caption("No modules completed yet.")

    achievements = get_achievements(progress)
    with st.sidebar.expander("🏆 Achievements", expanded=False):
        if achievements:
            for badge in achievements:
                st.write(f"{badge['icon']} **{badge['name']}**")
                st.caption(badge["desc"])
        else:
            st.caption("No achievements unlocked yet.")


def main() -> None:
    """Render the app and manage local progress lifecycle."""
    # Load + persist in session
    if "qa_progress" not in st.session_state:
        progress = load_progress()
        # Validate loaded progress
        is_valid, issues = validate_progress(progress)
        if not is_valid:
            st.sidebar.error("⚠️ Progress data has issues:")
            for issue in issues:
                st.sidebar.warning(f"- {issue}")
            st.session_state.qa_progress_invalid = True
        st.session_state.qa_progress = progress

    progress = st.session_state.qa_progress
    progress = touch_activity(progress)
    progress = _persist_progress(progress)

    _render_sidebar(progress)

    menu = ["Home", *MODULES, "Paper Trading", "Strategy Builder"]
    choice = st.sidebar.radio("Navigation", menu)

    if choice == "Home":
        st.title("Welcome to QuantAcademy 🎓")
        st.markdown(
            """
> Interactive quantitative finance learning platform.

### 🎯 Your Journey Starts Here
Select a module from the sidebar to begin learning.
            """
        )

        stats = get_stats(progress, len(MODULES))
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Current Streak (days)", stats["streak_days"])
        c2.metric("XP Earned", stats["xp"])
        c3.metric("Modules Completed", f"{stats['modules_completed']}/{stats['modules_total']}")
        c4.metric("Completion Rate", f"{stats['completion_rate']}%")

        st.divider()
        st.subheader("Quick actions")
        if st.button("Mark today as active (streak)"):
            progress = touch_activity(progress)
            progress = _persist_progress(progress)
            st.success("Activity saved.")

    elif choice in MODULES:
        st.title(choice)
        st.info("🚧 This module is currently under development.")

        col1, col2 = st.columns([1, 2])
        with col1:
            already = choice in progress.completed_modules
            st.write("### ✅ Completion")
            st.write(
                "Mark this module as complete to earn XP (local progress only)."
            )
            st.write(f"**Reward:** {DEFAULT_XP_PER_MODULE} XP")

            if already:
                st.success("You already completed this module.")
            if st.button(
                "Mark module complete", disabled=already, use_container_width=True
            ):
                progress = complete_module(progress, choice)
                progress = _persist_progress(progress)
                st.success("Saved! XP awarded.")

        with col2:
            st.write("### Next steps")
            st.markdown(
                """
- Add lesson content under `curriculum/` (not created yet)
- Add quizzes/exercises + autograder
- Replace JSON storage with a DB when multi-user
                """
            )

    else:
        st.title(choice)
        st.info("🚧 This feature is currently under development. Check back soon!")


if __name__ == "__main__":
    main()
