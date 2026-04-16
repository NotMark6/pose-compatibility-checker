import os
from typing import Dict, List, Tuple

# =========================
# ROLE DEFINITIONS
# =========================
roles: Dict[str, Dict[str, object]] = {
    "Cis Female": {
        "penis": False, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 1.0, "reach": 1.0,
    },
    "Cis Female (Athletic)": {
        "penis": False, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 1.3, "reach": 1.1,
    },
    "Cis Female (Curvy)": {
        "penis": False, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 0.8, "reach": 0.9,
    },
    "Cis Female (Petite)": {
        "penis": False, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 1.1, "reach": 0.8,
    },

    "Cis Male": {
        "penis": True, "vagina": False, "breasts": False,
        "hair": False, "flexibility": 1.0, "reach": 1.0,
    },
    "Cis Male (Large penis size)": {
        "penis": True, "vagina": False, "breasts": False,
        "hair": False, "flexibility": 0.9, "reach": 1.0,
    },
    "Cis Male (Small penis size)": {
        "penis": True, "vagina": False, "breasts": False,
        "hair": False, "flexibility": 1.1, "reach": 1.0,
    },

    "Eunuch": {
        "penis": False, "vagina": False, "breasts": False,
        "hair": False, "flexibility": 1.0, "reach": 1.0,
    },
    "Futanari": {
        "penis": True, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 1.0, "reach": 1.0,
    },
    "Mastectomy Survivor": {
        "penis": False, "vagina": True, "breasts": False,
        "hair": True, "flexibility": 1.0, "reach": 1.0,
    },

    "Trans Man (Pre-op)": {
        "penis": False, "vagina": True, "breasts": True,
        "hair": True, "flexibility": 1.0, "reach": 1.0,
    },
    "Trans Woman (Pre-op)": {
        "penis": True, "vagina": False, "breasts": True,
        "hair": True, "flexibility": 1.0, "reach": 1.0,
    },
}

# =========================
# POSITION
# Edit per position
# =========================
position: Dict[str, object] = {
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
    "requires_flexibility": False,
    "chest_access": False,
    "B_can_reach_up": True,  #  VERY IMPORTANT
    "genital_access_B_to_A": True,
}

# =========================
# ACTION TAGS
# Replace these generic actions
# with your own local labels
# =========================
act_tags: Dict[str, List[str]] = {
    "Scratching": ["needs_reach"],

    "Vaginal Penetration": ["needs_penis", "needs_vagina", "needs_rear_entry"],
    "Anal Penetration": ["needs_penis", "needs_rear_entry"],

    "Fellatio": ["needs_penis", "needs_face", "needs_oral_alignment"],
    "Deep Throat": ["needs_penis", "needs_face", "needs_oral_alignment"],

    "Cunnilingus": ["needs_vagina", "needs_face", "needs_oral_alignment"],
    "Analingus": ["needs_face", "needs_oral_alignment"],

    "Kissing": ["needs_face"],
    "Neck Kissing": ["needs_face"],

    "Nipple Stimulation (Oral)": ["needs_breasts", "needs_face"],
    "Breast Sucking": ["needs_breasts", "needs_face"],

    "Titjob": ["actor_needs_breasts", "target_needs_penis", "needs_chest_alignment"],

    "Handjob": ["needs_hand", "needs_genital_access", "target_needs_penis"],

    "Vaginal Fingering": ["needs_vagina", "needs_hand", "needs_genital_access"],
    "Anal Fingering": ["needs_hand", "needs_butt_access", "needs_rear_entry"],

    "Breast Stimulation (Manual)": ["needs_breasts", "needs_hand"],
    "Nipple Stimulation (Manual)": ["needs_hand", "needs_chest_access"],

    "Choking": ["needs_reach", "needs_neck_access"],
    "Hair Pulling": ["needs_hand", "needs_head_access"],
    "Spanking": ["needs_hand", "needs_butt_access", "needs_rear_swing"],
    "Biting": ["needs_face"],

    "Footjob": ["needs_penis", "target_needs_penis", "needs_feet"],
}

directions = ["A->B", "B->A"]


# =========================
# HELPERS
# =========================
def get_actor_target(
    A: Dict[str, object],
    B: Dict[str, object],
    direction: str,
) -> Tuple[Dict[str, object], Dict[str, object]]:
    return (A, B) if direction == "A->B" else (B, A)


def role_labels(direction: str) -> Tuple[str, str]:
    return ("Role A", "Role B") if direction == "A->B" else ("Role B", "Role A")


# =========================
# CHECK FUNCTION - MAIN LOGIC FOR CHECKING ACTS
# =========================
def check_act(A, B, act_name, direction):
    actor, target = get_actor_target(A, B, direction)
    actor_label, target_label = role_labels(direction)
    tags = act_tags[act_name]

    # =========================
    # FAIL CONDITIONS
    # =========================

    # Anatomy checks
    # DEBUGGING OUTPUT FOR SPANKING    
    if act_name == "Spanking":
        print(
        "DEBUG SPANKING",
        direction,
        "needs_hand=", "needs_hand" in tags,
        "needs_butt_access=", "needs_butt_access" in tags,
        "needs_rear_swing=", "needs_rear_swing" in tags,
        "A_can_reach_down=", position.get("A_can_reach_down", False),
        "B_can_reach_up=", position.get("B_can_reach_up", False),
        "butt_access_A_to_B=", position.get("butt_access_A_to_B", False),
        "butt_access_B_to_A=", position.get("butt_access_B_to_A", False),
        "rear_swing_access_A_to_B=", position.get("rear_swing_access_A_to_B", False),
        "rear_swing_access_B_to_A=", position.get("rear_swing_access_B_to_A", False),
    )
        
    if act_name == "Spanking":
        print("CHECK", direction,
          position.get("A_can_reach_down"),
          position.get("butt_access_A_to_B"),
          position.get("rear_swing_access_A_to_B"))
    
    if "needs_rear_swing" in tags:
        if direction == "A->B" and not position.get("rear_swing_access_A_to_B", False):
            return False, f"{actor_label} cannot perform this action due to movement restriction"
        if direction == "B->A" and not position.get("rear_swing_access_B_to_A", False):
            return False, f"{actor_label} cannot perform this action due to movement restriction"

    if "needs_chest_access" in tags:
        if not position.get("chest_access", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}'s chest"
    
    if "needs_head_access" in tags:
        if direction == "A->B" and not position.get("head_access_A_to_B", False):
            return False, ...
        if direction == "B->A" and not position.get("head_access_B_to_A", False):
            return False, ...
    
    if "needs_rear_entry" in tags:
        if not position.get("rear_entry_angle", False):
            return False, f"{actor_label} cannot perform this action due to positioning angle"
    
    if "needs_chest_alignment" in tags:
        if not position.get("chest_alignment", False):
            return False, f"{actor_label} cannot perform this action due to body alignment"
    
    if "needs_oral_alignment" in tags:
     if not position.get("oral_alignment", False):
        return False, f"{actor_label} cannot perform this action due to body orientation"
    
    if "needs_chest_access" in tags and not position.get("chest_access", False):
        return False, f"{actor_label} cannot align chest with {target_label.lower()}"

    if "needs_butt_access" in tags:
        if direction == "A->B" and not position.get("butt_access_A_to_B", False):
            return False, f"{actor_label} cannot access {target_label.lower()}'s backside"
        if direction == "B->A" and not position.get("butt_access_B_to_A", False):
            return False, f"{actor_label} cannot access {target_label.lower()}'s backside"

    if "needs_penis" in tags and not actor.get("penis", False):
        return False, f"{actor_label} has no penis"

    if "needs_vagina" in tags and not target.get("vagina", False):
        return False, f"{target_label} has no vagina"

    if "needs_breasts" in tags and not target.get("breasts", False):
        return False, f"{target_label} has no breasts"

    # Actor/target-specific checks
    if "actor_needs_breasts" in tags and not actor.get("breasts", False):
        return False, f"{actor_label} has no breasts"

    if "target_needs_penis" in tags:
        if not target.get("penis", False):
            return False, f"{target_label} has no penis"

    # Position checks
       # =========================
    # POSITION CHECKS (FIXED)
    # =========================

    if "needs_face" in tags and not position.get("face_access", False):
        return False, "No face access in this position"

    if "needs_alignment" in tags and not position.get("hips_aligned", False):
        return False, "Hips are not aligned"

    if "needs_hair" in tags and not target.get("hair", True):
        return False, f"{target_label} has no hair"

    if "needs_genital_access" in tags:
        if direction == "A->B" and not position.get("genital_access_A_to_B", True):
            return False, f"{actor_label} cannot access {target_label.lower()}'s lower body"
        if direction == "B->A" and not position.get("genital_access_B_to_A", False):
            return False, f"{actor_label} cannot access {target_label.lower()}'s lower body"

    if "needs_neck_access" in tags:
        if direction == "A->B" and not position.get("neck_access_A_to_B", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}'s neck"
        if direction == "B->A" and not position.get("neck_access_B_to_A", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}'s neck"

    if "needs_head_access" in tags:
        if direction == "A->B" and not position.get("head_access_A_to_B", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}'s head"
        if direction == "B->A" and not position.get("head_access_B_to_A", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}'s head"

    if "needs_chest_access" in tags and not position.get("chest_access", False):
        return False, f"{actor_label} cannot align chest with {target_label.lower()}"


    # =========================
    # REACH CHECKS (FIXED)
    # =========================
    if "needs_feet" in tags:
        if direction == "A->B" and not position.get("A_can_use_feet", False):
            return False, f"{actor_label} cannot use feet in this position"
        if direction == "B->A" and not position.get("B_can_use_feet", False):
            return False, f"{actor_label} cannot use feet in this position"

    if "needs_hand" in tags:
        if direction == "A->B" and not position.get("A_can_reach_down", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"
        if direction == "B->A" and not position.get("B_can_reach_up", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"

    if "needs_reach" in tags:
        if direction == "A->B" and not position.get("A_can_reach_down", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"
        if direction == "B->A" and not position.get("B_can_reach_up", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"
    

    # =========================
    # SUCCESS TEXT (YOUR FORMAT)
    # =========================

    if act_name == "Vaginal Penetration":
        return True, f"{actor_label} has a penis and can reach {target_label.lower()}'s vagina"

    if act_name == "Anal Penetration":
        return True, f"{actor_label} has a penis and can reach {target_label.lower()}'s anus"

    if act_name == "Vaginal Fingering":
        return True, f"{actor_label} can reach to finger {target_label.lower()}'s vagina"

    if act_name == "Anal Fingering":
        return True, f"{actor_label} can reach {target_label.lower()}'s anus"

    if act_name == "Breast Stimulation (Manual)":
        return True, f"{actor_label} can reach {target_label.lower()}'s breasts"

    if act_name == "Nipple Stimulation (Manual)":
        return True, f"{actor_label} can reach {target_label.lower()}'s nipples"

    if act_name == "Hair Pulling":
        return True, f"{actor_label} can pull {target_label.lower()}'s hair easily"

    if act_name == "Choking":
        return True, f"{actor_label} can reach {target_label.lower()}'s neck"

    if act_name == "Titjob":
        return True, f"{actor_label} can use breasts to stimulate {target_label.lower()}'s penis"

    if act_name == "Handjob":
        return True, f"{actor_label} can stimulate {target_label.lower()}'s genitals by hand"

    if act_name == "Scratching":
        return True, f"{actor_label} can reach {target_label.lower()}"

    if act_name == "Spanking":
        return True, f"{actor_label} can access {target_label.lower()}'s backside"

    if act_name == "Footjob":
        return True, f"{actor_label} can use feet to stimulate {target_label.lower()}"

    # fallback (rare)
    return True, f"{actor_label} can perform {act_name} due to position and reach"


# =========================
# MAIN RUN
# =========================
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "output.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        total_checks = 0
        total_possible = 0
        total_impossible = 0

        for A_name, A in roles.items():
            for B_name, B in roles.items():
                possible_acts: List[Tuple[str, str, str]] = []

                for act_name in act_tags:
                    for direction in directions:
                        total_checks += 1
                        result, reason = check_act(A, B, act_name, direction)

                        if result:
                            total_possible += 1
                            possible_acts.append((direction, act_name, reason))
                        else:
                            total_impossible += 1

                if possible_acts:
                    f.write(f"\n{A_name} A + {B_name} B\n")
                    for direction, act_name, reason in possible_acts:
                        f.write(f"{direction} {act_name}\n")
                        f.write(f"{reason}\n")

        f.write("\n=== SUMMARY ===\n")
        f.write(f"Total checks: {total_checks}\n")
        f.write(f"Total possible: {total_possible}\n")
        f.write(f"Total impossible: {total_impossible}\n")

    print(f"FILE WRITTEN HERE: {output_path}")