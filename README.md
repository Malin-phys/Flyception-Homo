
# Flyception-Homo 🧠🎥🏳️‍🌈

**蝇梦空间：野兽先辈的求偶回路**

> "逸一时，误一世。多巴胺分泌过头了，我要晕了。"

[![Status](https://img.shields.io/badge/Status-恶臭开发中-red)](https://github.com/)
[![Neurons](https://img.shields.io/badge/Neurons-166,700-blue)](https://www.janelia.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 项目简介
`Flyception-Homo` 是一个基于 **MaleCNS v1.0（成年雄性果蝇全脑连接组）** 的神经-视频生成框架。
它不是为了发Nature，而是为了探索一个终极哲学命题：**当一只雄性果蝇的求偶回路（P1神经元）和恐惧回路（巨纤维神经元）同时激活时，它眼中的世界是什么样的？**

本项目将果蝇的实时神经放电映射为AI视频生成参数（Prompt），专门用于拍摄两隻雄性果蝇在“昏睡红茶（发酵糖水）”旁的《蝇梦空间》。

## ✨ 核心特性
- **趋光性剪辑**：R1-R8光感受器激活 -> 画面曝光度+200%，切暖色调。
- **多巴胺陷阱**：PAM集群放电 -> 自动生成“好啊，来啊”的LLM字幕。
- **恐惧蒙太奇**：巨纤维神经元触发 -> 画面Glitch扭曲，恐怖片滤镜。
- **睡眠重放（蝇梦）**：慢波振荡 -> 把失败的求偶记忆和天敌记忆混合，生成梦境。

## 🚀 快速开始
1. 克隆本项目：
   ```bash
   git clone https://github.com/yourname/Flyception-Homo.git
   cd Flyception-Homo
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行模拟器（请确保已下载MaleCNS连接组数据）：
   ```bash
   python scripts/fly_brain_reader.py --config configs/homo_config.json
   ```
⚠️ 伦理声明
本项目中所有果蝇均为数字模拟（Digital Twin）。没有真实果蝇在拍摄过程中受到伤害（虽然它们可能被远野拒绝了）。

🙏 致谢
感谢 FlyWire 和 Janelia 研究园区提供的开源连接组数据。
感谢 野兽先辈 提供的神经回路灵感。
感谢 远野 贡献的逃避反射数据


---

### 📦 `requirements.txt` （依赖库）

```text
numpy==1.26.0
pynput==1.7.6
python-osc==1.9.0
opencv-python==4.9.0
requests==2.31.0
