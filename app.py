import streamlit as st
import mainV2

# shortcuts to your existing code
roles = mainV2.roles
act_tags = mainV2.act_tags
check_act = mainV2.check_act
directions = mainV2.directions

# =========================
# POSITIONS (START SMALL)
# =========================
positions = {}

positions["Rodeo"] = {
    "faces_aligned": False,
    "hips_aligned": True,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "A_facing_away": True,
    "neck_access_A_to_B": False,
    "neck_access_B_to_A": False,
    "head_access_A_to_B": False,
    "head_access_B_to_A": False,
    "face_access": False,
    "chest_access": False,
    "butt_access": False,
    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Lazy Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Lying Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Open Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Planted Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Squatting Open Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Squatting Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Standing Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Standing Twisted Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}

positions["Twisted Rodeo"] = {
    **positions["Rodeo"],
    "B_can_reach_up": False,
}



positions["Missionary"] = {
    "faces_aligned": True,
    "hips_aligned": True,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True,
    "head_access_A_to_B": True,
    "head_access_B_to_A": True,
    "face_access": True,
    "chest_access": True,
    "butt_access": False,
    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Closed Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Folded Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Kneeling Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Mating Press"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Mixed Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Open Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Oystered Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Split Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Tilted Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Tucked Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Tucked Missionary 180"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Twisted Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Upright Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}

positions["Wrapped Missionary"] = {
    **positions["Missionary"],
    "B_can_reach_up": False,
}



positions["Lotus"] = {
    "faces_aligned": True,
    "hips_aligned": True,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "A_facing_away": False,
    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True, 
    "head_access_A_to_B": True,
    "head_access_B_to_A": True,
    "face_access": True,
    "chest_access": True,
    "butt_access_A_to_B": True,
    "butt_access_B_to_A": True,
    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
    "oral_alignment": False,
    "chest_alignment": False,
    "rear_entry_angle": True,
    "rear_swing_access_A_to_B": True,
    "rear_swing_access_B_to_A": False,
    "A_can_use_feet": False,
    "B_can_use_feet": False,
}

positions["Blossoming (Utphallaka)"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Crabby Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Folded Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Kneeling Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Lazy Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Mixed Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Wrapped Lotus"] = {
    **positions["Lotus"],
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,
}

positions["Manual Base(Face-to-Face Seated Mutual)"] = {
    "faces_aligned": True,
    "hips_aligned": False,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "A_facing_away": False,
    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True,
    "head_access_A_to_B": True,
    "head_access_B_to_A": True,
    "face_access": True,
    "chest_access": False,
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": False,
    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Head-to-Toe Mutual"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Intercrural (Between Thighs)"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
}

positions["Kneeling Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Kneeling Reach-Around"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Lap Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Lying Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Mutual Missionary (Hand)"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Over the Shoulder Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Reach Around (Standing)"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Side-by-Side Mutual Masturbation"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Sitting Reach-Around"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Spooning Reach-Around"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Standard Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Standing Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Straddling Handjob"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Titjob / Chest Stimulation"] = {
    **positions["Manual Base(Face-to-Face Seated Mutual)"],
    "B_can_reach_up": False,
}

positions["Full Nelson"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": False,

    "A_facing_away": False,

    "face_access": False,

    "neck_access_A_to_B": True,
    "neck_access_B_to_A": False,

    "head_access_A_to_B": True,
    "head_access_B_to_A": False,

    "chest_access": False,

    # 🔥 Directional
    "butt_access_A_to_B": True,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": False,
}

positions["Full Nelson (Knees)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": True,
}
positions["Full Nelson (Knees, Arms & Head)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": True,
}
positions["Full Nelson (Knees & Head)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": True,
}

positions["Kneeling Full Nelson"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": True,
}

positions["Kneeling Full Nelson (Knees)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}

positions["Kneeling Full Nelson (Knees, Arms & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}

positions["Kneeling Full Nelson (Knees & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}

positions["Laying Back Full Nelson"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,
    "genital_access_B_to_A": True,
}

positions["Laying Back Full Nelson (Knees)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,
    "genital_access_B_to_A": True,
}

positions["Laying Back Full Nelson (Knees, Arms & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,
    "genital_access_B_to_A": True,
}

positions["Laying Back Full Nelson (Knees & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,
    "genital_access_B_to_A": True,
}

positions["Sitting Full Nelson"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}

positions["Sitting Full Nelson (Knees)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}
positions["Sitting Full Nelson (Knees, Arms & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}
positions["Sitting Full Nelson (Knees & Head)"] = {
    **positions["Full Nelson"],
    "B_can_reach_up": True,   # slight regain of reach
}

positions["Suspended Full Nelson"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": False,  # instability
}

positions["Suspended Full Nelson (Knees)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": False,  # instability
}

positions["Suspended Full Nelson (Knees, Arms & Head)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": False,  # instability
}

positions["Suspended Full Nelson (Knees & Head)"] = {
    **positions["Full Nelson"],
    "A_can_reach_down": False,  # instability
}



positions["Pile Driver"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": False,

    "A_facing_away": False,

    "face_access": False,

    "neck_access_A_to_B": False,
    "neck_access_B_to_A": False,

    "head_access_A_to_B": False,
    "head_access_B_to_A": False,

    "chest_access": False,

    # 🔥 Directional
    "butt_access_A_to_B": True,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": False,
}

positions["Grounded Pile Driver"] = {
    **positions["Pile Driver"],
    "A_can_reach_down": True,  # more stable
}

positions["Pile Driver 180"] = {
    **positions["Pile Driver"],
    "genital_access_A_to_B": True,  # still aligned
}

positions["Squatting Pile Driver"] = {
    **positions["Pile Driver"],
    "A_can_reach_down": False,  # balance loss
}

positions["Squatting Pile Driver 180"] = {
    **positions["Pile Driver"],
    "A_can_reach_down": False,  # balance loss
}

positions["Twisted Pile Driver"] = {
    **positions["Pile Driver"],
    "hips_aligned": False,  # twist reduces alignment
}


positions["Saint"] = {
    "faces_aligned": True,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": True,

    "A_facing_away": False,

    "face_access": True,

    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True,

    "head_access_A_to_B": True,
    "head_access_B_to_A": True,

    "chest_access": True,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,  # similar to Lotus behavior

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Crabby Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}

positions["Folded Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}
positions["Kneeling Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}
positions["Kneeling Saint 180"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}

positions["Lazy Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}

positions["Mixed Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": False,
    "B_can_reach_up": False,
}

positions["Saint 180"] = {
    **positions["Saint"],
    "faces_aligned": False,
}

positions["Wrapped Saint"] = {
    **positions["Saint"],
    "A_can_reach_down": True,
}



positions["Scissors"] = {
    "faces_aligned": True,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": True,

    "A_facing_away": False,

    "face_access": True,

    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True,

    "head_access_A_to_B": True,
    "head_access_B_to_A": True,

    "chest_access": True,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Classic Tribbing"] = {
    **positions["Scissors"],
    "face_access": True,
}
positions["Crabby Scissors"] = {
    **positions["Scissors"],
    "face_access": True,
}
positions["Kneeling Scissors"] = {
    **positions["Scissors"],
    "face_access": True,
}
positions["Missionary Scissors"] = {
    **positions["Scissors"],
    "face_access": True,
}
positions["Scissored Flagpole"] = {
    **positions["Scissors"],
    "face_access": True,
}

positions["Sitting Scissors"] = {
    **positions["Scissors"],
    "face_access": True,
}

positions["Twisted Kneeling Scissors"] = {
    **positions["Scissors"],
    "B_can_reach_up": False,
}

positions["Upright Scissor"] = {
    **positions["Scissors"],
    "B_can_reach_up": False,
}

positions["Wrapped Scissors"] = {
    **positions["Scissors"],
    "B_can_reach_up": False,
}


positions["Sinner"] = {
    "faces_aligned": True,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": False,  # 🔥 key difference

    "A_facing_away": False,

    "face_access": True,

    "neck_access_A_to_B": True,
    "neck_access_B_to_A": False,

    "head_access_A_to_B": True,
    "head_access_B_to_A": False,

    "chest_access": True,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Closed Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}
positions["Folded Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}
positions["Kneeling Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}
positions["Planted Closed Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}
positions["Planted Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}
positions["Pressed Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}

positions["Split Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}

positions["Tilted Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}

positions["Tucked Sinner"] = {
    **positions["Sinner"],
    "B_can_reach_up": False,
}

positions["Wrapped Sinner"] = {
    **positions["Sinner"],
    "hips_aligned": True,
    "B_can_reach_up": True
}



positions["Spoon"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": False,
    "B_can_reach_up": True,

    "A_facing_away": True,

    "face_access": False,

    "neck_access_A_to_B": False,
    "neck_access_B_to_A": True,

    "head_access_A_to_B": False,
    "head_access_B_to_A": True,

    "chest_access": False,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,

    "genital_access_A_to_B": False,
    "genital_access_B_to_A": True,
}

positions["Bent Spoon"] = {
    **positions["Spoon"],
    "genital_access_B_to_A": True,
}

positions["Bipolar Spoon"] = {
    **positions["Spoon"],
    "genital_access_B_to_A": True,
}

positions["Box Position (Parshva Samputa)"] = {
    **positions["Spoon"],
    "chest_access": True
}

positions["Crossed Spoon"] = {
    **positions["Spoon"],
    "genital_access_B_to_A": True,
}

positions["Wrapped Spoon"] = {
    **positions["Spoon"],
    "hips_aligned": False,
}

positions["Driver's Open Lap Dance"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": False,   # steering + seat restriction
    "B_can_reach_up": True,

    "A_facing_away": False,

    "face_access": False,

    "neck_access_A_to_B": False,
    "neck_access_B_to_A": True,

    "head_access_A_to_B": False,
    "head_access_B_to_A": True,

    "chest_access": False,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,

    "genital_access_A_to_B": False,
    "genital_access_B_to_A": True,
}

positions["Driver's Road Head"] = {
    **positions["Driver's Open Lap Dance"],
    "genital_access_B_to_A": True,
}

positions["Shotgun Base"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": True,

    "A_facing_away": False,

    "face_access": False,

    "neck_access_A_to_B": False,
    "neck_access_B_to_A": False,

    "head_access_A_to_B": False,
    "head_access_B_to_A": False,

    "chest_access": False,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
}

positions["Shotgun Doggy"] = {
    **positions["Shotgun Base"],
    "A_facing_away": True,

    "butt_access_A_to_B": True,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": False,
}

positions["Shotgun Open Missionary"] = {
    **positions["Shotgun Base"],
    "faces_aligned": True,

    "neck_access_A_to_B": True,
    "neck_access_B_to_A": True,

    "head_access_A_to_B": True,
    "head_access_B_to_A": True,

    "chest_access": True,
}

positions["Shotgun Rodeo"] = {
    **positions["Shotgun Base"],
    "A_facing_away": True,
    "A_can_reach_down": False,
    "face_access": False,

    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,

    "genital_access_B_to_A": True,
}

positions["Shotgun Road Head"] = {
    **positions["Shotgun Base"],
    "genital_access_B_to_A": True,
    "butt_access_B_to_A": True,
    "A_can_reach_down": False,
}

positions["Shotgun Open Lap Dance"] = {
    **positions["Shotgun Base"],
    "butt_access_B_to_A": True,
}

positions["Shotgun Sinner"] = {
    **positions["Shotgun Base"],
    "faces_aligned": True,
    "B_can_reach_up": False,
}

positions["Shotgun Tucked Groundhog"] = {
    **positions["Shotgun Base"],
    "B_can_reach_up": False,
    "A_can_reach_down": False,
}

positions["Shotgun Servant"] = {
    **positions["Shotgun Base"],
    "A_can_reach_down": False,
    "B_can_reach_up": True,
}

positions["Shotgun Collapsed Cowgirl"] = {
    **positions["Shotgun Base"],
    "A_can_reach_down": False,
}

positions["Shotgun Open Butterfly"] = {
    **positions["Shotgun Base"],
    "chest_access": True,
}

positions["Wheelbarrow"] = {
    "faces_aligned": False,
    "hips_aligned": True,

    "A_can_reach_down": True,
    "B_can_reach_up": False,

    "A_facing_away": True,

    "face_access": False,

    "neck_access_A_to_B": False,
    "neck_access_B_to_A": False,

    "head_access_A_to_B": False,
    "head_access_B_to_A": False,

    "chest_access": False,

    # 🔥 Directional (key for this family)
    "butt_access_A_to_B": True,
    "butt_access_B_to_A": False,

    "genital_access_A_to_B": True,
    "genital_access_B_to_A": False,

    "rear_entry_angle": True,
    "rear_swing_access_A_to_B": True,
}

positions["Kneeling Wheelbarrow"] = {
    **positions["Wheelbarrow"],
    "A_can_reach_down": True,
}

positions["Sitting Wheelbarrow"] = {
    **positions["Wheelbarrow"],
    "B_can_reach_up": False,
}

positions["Supported Wheelbarrow"] = {
    **positions["Wheelbarrow"],
    "B_can_reach_up": False,
}

positions["Supported Kneeling Wheelbarrow"] = {
    **positions["Wheelbarrow"],
    "A_can_reach_down": True,
    "B_can_reach_up": False,
}


# =========================
# UI
# =========================
st.title("Pose Compatibility Checker")

role_A = st.selectbox("Role A", list(roles.keys()))
role_B = st.selectbox("Role B", list(roles.keys()))
pose = st.selectbox("Position", list(positions.keys()))

if st.button("Generate"):

    # update position dynamically
    mainV2.position = positions[pose]

    A = roles[role_A]
    B = roles[role_B]

    st.subheader(f"{role_A} (A) + {role_B} (B)")

    for act in act_tags:
        for direction in directions:
            result, reason = check_act(A, B, act, direction)
            #if act == "Spanking":
                #st.write("DEBUG SPANKING", direction, result, reason)
            if result:
                st.write(f"**({direction.replace('->','→')}) {act} - {reason}**")
