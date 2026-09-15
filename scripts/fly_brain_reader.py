import time
import random
import json
from neuro_to_video import render_video
from subtitle_generator import generate_subtitle

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def simulate_neural_activity():
    """
    模拟从 MaleCNS v1.0 连接组读取的实时神经放电频率（单位：Hz）
    在此处接入真实的模拟器 API，比如 FlyBrain 或 NeuroMechFly。
    """
    return {
        "P1_Neuron": random.uniform(0, 100),
        "Giant_Fiber": random.uniform(0, 100),
        "PAM_Dopamine": random.uniform(0, 100),
        "Sleep_Slow_Wave": random.uniform(0, 1)
    }

def main():
    print("🐛 [Flyception-Homo] 启动果蝇全脑模拟器...")
    print("🍵 正在注入发酵糖水（昏睡红茶）气味...")
    config = load_config("../configs/homo_config.json")
    
    frames = 0
    while frames < 100:
        activity = simulate_neural_activity()
        
        # 判断当前主导的神经状态
        if activity["Giant_Fiber"] > 70:
            state = "FEAR"
            print(f"⚠️ [巨纤维神经元活跃] 远野正在逃跑！当前频率: {activity['Giant_Fiber']:.2f} Hz")
        elif activity["P1_Neuron"] > 60 and activity["PAM_Dopamine"] > 50:
            state = "MATING"
            print(f"🕺 [P1求偶回路激活] 野兽先辈开始振动翅膀！当前多巴胺: {activity['PAM_Dopamine']:.2f} Hz")
        elif activity["Sleep_Slow_Wave"] > 0.8:
            state = "DREAM"
            print("💤 [慢波振荡] 进入蝇梦空间，记忆开始重放...")
        else:
            state = "FORAGING"
            print("🚶 [中央复合体] 漫无目的地游荡。")
            
        render_video(state, activity, config)
        subtitle = generate_subtitle(activity, state)
        if subtitle:
            print(f"💬 [字幕] {subtitle}")
            
        frames += 1
        time.sleep(0.5) # 模拟实时帧率

if __name__ == "__main__":
    main()
