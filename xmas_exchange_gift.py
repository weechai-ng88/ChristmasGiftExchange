import random
import streamlit as st

# Function to draw lots
def draw_lots(participants):
    """
    Draw lots for a Christmas gift exchange.
    Ensures no one is assigned to themselves.
    
    Args:
    participants (list): List of participant names.

    Returns:
    dict: A dictionary mapping each participant to their recipient.
    """
    givers = participants[:]
    receivers = participants[:]

    while True:
        random.shuffle(receivers)
        # Check if any giver is assigned to themselves
        if all(giver != receiver for giver, receiver in zip(givers, receivers)):
            break

    return dict(zip(givers, receivers))


# Streamlit app
st.title("🎄🎁 Christmas Gift Exchange App")

# Add Christmas music
st.markdown(
    """
    <audio controls autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-thejazzpiano.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for participant list
if "participants" not in st.session_state:
    st.session_state.participants = []

# Input to add participants
with st.form("add_participant"):
    new_participant = st.text_input("Add a participant's name:")
    add_button = st.form_submit_button("Add Name")
    if add_button and new_participant:
        st.session_state.participants.append(new_participant.strip())
        st.success(f"Added: {new_participant}")

# Display the list of participants
st.write("### Current Participants:")
if st.session_state.participants:
    for i, name in enumerate(st.session_state.participants, start=1):
        st.write(f"{i}. {name}")
else:
    st.info("No participants added yet. Add names above.")

# Button to clear the list
if st.button("Clear List"):
    st.session_state.participants = []
    st.success("Participant list cleared.")

# Button to draw lots
if st.button("Draw Lots"):
    if len(st.session_state.participants) < 2:
        st.error("Please add at least 2 participants to draw lots.")
    else:
        result = draw_lots(st.session_state.participants)
        st.write("### Gift Exchange Results:")
        for giver, receiver in result.items():
            st.write(f"🎅 {giver} → 🎁 {receiver}")
