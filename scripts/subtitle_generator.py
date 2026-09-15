def generate_subtitle(activity, state):
    if state == "MATING" and activity["PAM_Dopamine"] > 80:
        return "先辈：好啊，来啊！"
    if state == "FEAR" and activity["Giant_Fiber"] > 90:
        return "远野：你、你这个蝇，不对劲……"
    if state == "DREAM":
        return "（梦呓）我追逐光，光却把我推向另一只雄蝇的影子……"
    return None
