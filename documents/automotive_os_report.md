
# 车载操作系统（OS）市场调查报告

## 报告摘要

车载操作系统是汽车智能化的底层技术底座。全球市场呈现 **“安全域 QNX、座舱域 Android/鸿蒙/AliOS、高端车型全栈自研”** 的多元竞争格局。

**本报告中每个系统均包含系统名称、开发主体、技术架构（细分 ARM/x86 等）、硬件型号及厂商、官方文档链接、车企合作情况等必要维度。** 报告涵盖 BlackBerry QNX、Google Android Automotive OS、Automotive Grade Linux（AGL）、Tesla OS、Mercedes-Benz MB.OS、Volkswagen VW.OS、RHIVOS（红帽车载操作系统）、华为鸿蒙座舱（HarmonySpace）、斑马智行 AliOS、比亚迪 DiLink、蔚来 Banyan 共 11 个核心系统。


## 第一章 系统架构与硬件支持总览

下表汇总了各系统支持的指令集架构及代表性硬件芯片厂商：

| 操作系统 | 支持架构 | 典型硬件/芯片厂商 | 官方文档入口 |
|---------|---------|-----------------|------------|
| **BlackBerry QNX** | ARM（ARMv7/ARMv8/AArch64）、x86（x86-64）、PowerPC | ARM Cortex-A 系列、Intel、NXP（i.MX）、Qualcomm、AMD Ryzen Embedded、Renesas、NVIDIA（Jetson/Orin）、TI | [QNX 官网](https://www.qnx.com) |
| **Android Automotive OS** | ARM（ARMv8-A/ARM64）、x86 | Samsung Exynos Auto、NXP（i.MX）、Qualcomm Snapdragon、ARM Cortex 系列 | [Android Developers](https://developer.android.com/training/cars) |
| **AGL** | x86（x86-64）、ARM（arm32/arm64）、QEMU | Renesas（R-Car Gen3）、Raspberry Pi、NXP（i.MX）、Intel（MinnowBoard Max）、BeagleBone | [docs.automotivelinux.org](https://docs.automotivelinux.org) |
| **RHIVOS** | ARM（AArch64）、x86（x86-64） | Renesas（R-Car）、Qualcomm、NXP、Intel、TI、Arm | [RHIVOS Data Sheet](https://www.redhat.com/en/resources/in-vehicle-operating-system-datasheet) / [AutoSD](https://sigs.centos.org/automotive/) |
| **华为鸿蒙座舱** | ARM（ARMv7-A/V7A/泰山V120） | 华为麒麟 990A/9610（4核泰山V120 + 4核ARM Cortex-A55 + 达芬奇NPU） | [华为开发者联盟](https://developer.huawei.com/consumer/cn/overview/ICS) |
| **斑马智行 AliOS** | ARM（ARMv9.2）跨平台 | 紫光展锐 A8880、芯驰科技（X10）、高通、联发科、瑞萨、恩智浦 | [aliOS 官网](https://www.alios.cn) |
| **比亚迪 DiLink** | ARM | 高通骁龙（SM6350/SM7325 等） | [比亚迪 DiLink 开发者平台](https://developer.byd.com) |
| **蔚来 Banyan** | ARM | 高通骁龙 8295（NT3平台）/ 8155（NT2平台）、英伟达 Orin-X | [蔚来官网](https://www.nio.cn) |
| **Tesla OS** | x86（x86-64，AMD APU） | AMD Ryzen Embedded（NAPLES/ZEUS） | [Tesla 官网](https://www.tesla.cn) |
| **Mercedes-Benz MB.OS** | ARM | 英伟达 Orin、高通 Snapdragon 等 | [Mercedes-Benz 官网](https://www.mercedes-benz.com) |
| **Volkswagen VW.OS** | ARM | 高通 Snapdragon、英伟达 Orin、瑞萨 R-Car | [CARIAD 官网](https://www.cariad.technology) |

> **注：** 架构缩写速查——ARM：高级精简指令集处理器，常见于移动设备和嵌入式系统，以低功耗著称；ARMv7（32位）/ARMv8（64位）/AArch64（64位执行状态）为 ARM 架构版本。x86：英特尔开发的复杂指令集架构，常见于 PC 和服务器领域，性能强大；x86-64 为 64 位扩展版本。PowerPC：精简指令集架构，常见于嵌入式系统。QEMU：开源虚拟机/硬件模拟器，用于跨平台仿真。


## 第二章 国外车载操作系统公司及产品

### 2.1 BlackBerry QNX

| 维度 | 内容 |
|------|------|
| **系统名称** | QNX 实时操作系统（含 QNX Neutrino RTOS、QNX OS for Safety、QNX Hypervisor） |
| **开发主体** | BlackBerry 有限公司 |
| **技术架构** | **微内核架构**（Microkernel Architecture），已通过 ISO 26262 ASIL‑D 最高功能安全认证。QNX SDP 8.0 采用第五代微内核设计，支持对称多处理（SMP）和混合关键性部署 |
| **支持架构** | **ARM（ARMv7 / ARMv8 / AArch64）、x86（x86-64）、PowerPC** |
| **硬件/芯片厂商** | 支持主流 ARM 和 x86 硅芯片厂商的 SoC 及评估板，包括 ARM Cortex-A 系列、Intel、NXP（i.MX 系列）、Qualcomm、AMD Ryzen Embedded、Renesas、NVIDIA（Jetson/Orin）、TI 等 |
| **官方文档** | [QNX 官网](https://www.qnx.com) / [QNX 开发者文档](https://www.qnx.com/developers/docs/) / [QNX BSP Library](https://qnx.software/en/developers/get-started/board-support-packages) |
| **核心特点** | 微内核架构极致安全，虚拟化能力卓越，实时性业内领先，在仪表、安全域、ADAS/自动驾驶领域占据统治地位 |

**车企合作情况**：

- **大众集团 CARIAD**：授权使用 QNX OS for Safety 2.2 作为统一软件平台 VW.OS 的底层安全基础
- **福特、通用、丰田、宝马、奔驰、现代**等全球主要车企在其仪表、安全域及 ADAS 领域广泛采用 QNX
- **文远知行 WePilot**：集成 QNX 技术栈于 L2++ 级 ADAS 方案 WePilot 中，搭载于 **奇瑞星途星纪元 ES 与 ET** 车型
- **地平线**：基于征程®6 系列打造融合 QNX 实时操作系统的车载智能计算方案
- **芯驰科技**：联合推出搭载 QNX Hypervisor 8.0 的智能座舱解决方案


### 2.2 Google —— Android Automotive OS

| 维度 | 内容 |
|------|------|
| **系统名称** | Android Automotive OS |
| **开发主体** | Google（Alphabet Inc.） |
| **技术架构** | 基于 **Android 开源项目（AOSP）** 打造的完整车载操作系统，通过 **HAL（硬件抽象层）** 实现与底层硬件的解耦，独立于 Android Auto（手机映射）。采用 Linux 内核 + Android 框架层 + Automotive API + Google 服务（GAS） |
| **支持架构** | **ARM（ARMv8-A / ARM64）、x86**。AOSP 支持 arm64 和 x86 仿真器环境，硬件要求符合 Android 兼容性定义文档（CDD）中的 Automotive Requirements |
| **硬件/芯片厂商** | 与主流车规 SoC 厂商深度适配，包括 Samsung Exynos Auto V920（ARM Cortex-A78AE）、NXP（i.MX 系列）、Qualcomm Snapdragon 等 |
| **官方文档** | [Android Developers - Automotive](https://developer.android.com/training/cars) / [AOSP - Automotive](https://source.android.com/docs/automotive) |
| **核心特点** | 完整的 Google 生态（地图、语音助手、Play 商店），车企可深度定制 UI/UX，HAL 解耦实现软硬件独立演进 |

**车企合作情况**：

- **沃尔沃汽车**：2025 年 5 月与谷歌深化合作，成为 **Android Automotive 系统的主要开发合作伙伴**，率先导入 Android 15 与 Google Gemini AI 模型，旗舰 EX90 电动 SUV 搭载最新版 Android 15 上市
- **通用汽车**：2026 年宣布推出移除 CarPlay 的方案，全面转向自研系统 + Android Automotive 深度集成
- **福特、雷诺、本田、Stellantis**：均在不同车型上采用或计划采用 Android Automotive OS 作为智能座舱方案


### 2.3 Automotive Grade Linux（AGL）

| 维度 | 内容 |
|------|------|
| **系统名称** | Automotive Grade Linux（AGL） |
| **开发主体** | Linux Foundation 旗下的开源项目，由全球汽车制造商、供应商和技术公司共同协作 |
| **技术架构** | **基于 Linux 内核的开源软件平台**，采用五层软件架构：App/HMI 层、应用框架层、服务层、Linux 内核层、硬件适配层（BSP）。支持混合关键性部署，通过容器技术实现业务隔离 |
| **支持架构** | **x86（x86-64）、ARM（arm32 / arm64）**。参考板包括 QEMU、Renesas R-Car Gen 3（arm64）、Raspberry Pi 4（arm64），社区板包括 BeagleBone（arm32）、NXP i.MX 系列 |
| **硬件/芯片厂商** | Renesas（R-Car Gen3 系列）、Raspberry Pi、NXP（i.MX6/i.MX8）、Intel（MinnowBoard Max）、BeagleBone 等 |
| **官方文档** | [docs.automotivelinux.org](https://docs.automotivelinux.org) / [AGL 官网](https://www.automotivelinux.org) |
| **核心特点** | 开源免费无许可费用，车企可自由定制，更新迭代成本低，社区协作加速创新 |

**车企合作情况**：

- **丰田汽车**：所有丰田和雷克萨斯汽车的信息娱乐系统均使用 AGL（基于 Linux 的系统更新和升级成本更低、速度更快）
- **德赛西威**（Tier 1）：量产的车载信息娱乐系统和虚拟仪表大部分基于 Linux 平台开发
- **奔驰、尼桑、捷豹路虎、福特、马自达**等主流汽车品牌的 IVI 系统均不同程度基于 Linux 构建


### 2.4 RHIVOS（Red Hat In‑Vehicle Operating System）—— **本报告新增**

| 维度 | 内容 |
|------|------|
| **系统名称** | Red Hat In‑Vehicle Operating System（RHIVOS） |
| **开发主体** | Red Hat（红帽公司，IBM 旗下） |
| **技术架构** | **基于 Linux 内核的开源汽车专用操作系统**，采用“上游创新 + 下游安全认证”的双轨开源发展模式。上游为 AutoSD（Automotive Stream Distribution），下游为安全认证生产级产品。**集成 PREEMPT_RT 内核**实现确定低延迟实时调度，支持 ADAS 等时间敏感型工作负载。**功能安全认证**：通过 ISO 26262:2018 ASIL‑B 安全认证（Safety Element out of Context），并包含混合关键性安全认证（mixed-criticality claim），支持安全与非安全应用在同一 ASIL 认证的 Linux 内核上共存。**支持容器化部署**，隔离通过 Linux 原生能力实现，无需独立 Guest OS。**集成 SELinux 强制访问控制、Firewall、LUKS 磁盘加密、Secure Boot、TPM 集成和 Rollback Protection**等多层安全机制 |
| **支持架构** | **ARM AArch64** 和 **x86-64** 双架构 |
| **硬件/芯片厂商** | 硅芯片合作伙伴包括 **ARM、Intel、NXP、Qualcomm、Renesas、Texas Instruments**。安全认证启动时搭载 **Renesas 设备**，随后支持 **Qualcomm 设备**。可部署于 **bare‑metal 或虚拟机**等多种硬件平台 |
| **官方文档** | **官方 Data Sheet**：[Red Hat In‑Vehicle Operating System Data Sheet](https://www.redhat.com/en/resources/in-vehicle-operating-system-datasheet)<br>**上游社区**：[CentOS Automotive SIG - AutoSD Documentation](https://sigs.centos.org/automotive/)<br>**硬件支持**：[AutoSD Hardware Enablement](https://sigs.centos.org/automotive/autosd-10/hardware-enablement/index.html) |
| **核心特点** | 红帽是全球首家实现 **Linux 车规级功能安全认证** 的商业发行版厂商，在功能安全、实时性、开源生态之间实现了平衡。以 **“软件优先”开发范式** 实现软硬件解耦，车企可在硬件样机到货前就开始软件开发，“一次开发，多硬件部署”。计划于 **2025 年第三季度（Q3）正式量产发布** |

**车企合作情况**：

- **通用汽车（GM）**：红帽在该领域的第一家合作伙伴，将 RHIVOS 集成到其 Ultifi 软件平台中，无需再开发底层操作系统
- 红帽正以“共同设计、共同开发合作伙伴”模式与多家车企深度合作，共同开发车辆各域功能及应用工具
- 芯片生态方面，红帽已与瑞萨电子（Renesas）合作，将 RHIVOS 与瑞萨 R‑Car 软件开发套件（SDK）集成；同时积极与 ARM、Intel、NXP、Qualcomm、TI 等芯片厂商合作，推动硬件预认证工作


### 2.5 Tesla OS

| 维度 | 内容 |
|------|------|
| **系统名称** | Tesla OS |
| **开发主体** | Tesla, Inc.（特斯拉） |
| **技术架构** | **全栈自研封闭系统**。底层基于 Linux 内核重新开发，运行在 AMD x86 架构 APU（加速处理单元）之上。采用分域自研架构，涵盖 WiFi、蓝牙、以太网、音频、渲染引擎、OTA 等多个模块 |
| **支持架构** | **x86（x86-64）** —— AMD Ryzen Embedded 系列 |
| **硬件/芯片厂商** | AMD（NAPLES / ZEUS 车规级 APU）、自研 FSD 芯片（基于 ARM） |
| **官方文档** | Tesla 官网（部分开源代码发布于 GitHub） |
| **核心特点** | 行业最早实现全域 OTA 升级，封闭生态 + 高流畅度性能，软硬件垂直整合 |

**车企合作情况**：Tesla OS 完全自用于 Tesla 品牌旗下 Model S/3/X/Y 及 Cybertruck 等全系车型，不对外输出。


### 2.6 Mercedes-Benz MB.OS

| 维度 | 内容 |
|------|------|
| **系统名称** | Mercedes-Benz Operating System（MB.OS） |
| **开发主体** | Mercedes-Benz Group AG（梅赛德斯-奔驰集团） |
| **技术架构** | **全栈自研**，覆盖 **信息娱乐、自动驾驶、车身舒适、驾驶与充电** 四大车辆域。基于自研超级计算机 + 智能云架构。支持 OTA 全车域升级 |
| **支持架构** | **ARM**（适配英伟达 Orin 等） |
| **硬件/芯片厂商** | 英伟达 Orin 系列（自动驾驶域）、高通 Snapdragon 系列（座舱域） |
| **官方文档** | Mercedes-Benz 官网 |
| **核心特点** | 豪华车企全栈自研的代表，首搭全新 CLA 车型，整合微软与谷歌 AI 能力，中国市场引入豆包 AI 大模型 |

**车企合作情况**：MB.OS 仅搭载于梅赛德斯-奔驰品牌旗下车型，不对外输出。


### 2.7 Volkswagen VW.OS

| 维度 | 内容 |
|------|------|
| **系统名称** | VW.OS |
| **开发主体** | Volkswagen Group 旗下软件公司 CARIAD |
| **技术架构** | 基于 **AUTOSAR Adaptive 标准**，底层安全域授权使用 BlackBerry QNX OS for Safety 2.2 |
| **支持架构** | **ARM** |
| **硬件/芯片厂商** | 高通 Snapdragon、英伟达 Orin、瑞萨 R‑Car 等 |
| **官方文档** | CARIAD 官网 |
| **核心特点** | 曾为集团统一软件平台战略核心，后因技术挑战调整为开放合作的协调角色 |

**车企合作情况**：VW.OS 目前仍在大众内部推进，重点已转向开放合作——从 BlackBerry 授权 QNX 底层安全 OS，并积极与小鹏、Rivian 等合作伙伴共建软件能力。


## 第三章 国内车载操作系统公司及产品

### 3.1 华为 —— 鸿蒙座舱（HarmonySpace）

| 维度 | 内容 |
|------|------|
| **系统名称** | 鸿蒙座舱 HarmonySpace（车载版），核心底层为鸿蒙操作系统（HarmonyOS） |
| **开发主体** | 华为技术有限公司 |
| **技术架构** | **全栈自研微内核架构（Microkernel Architecture）** ，分布式设计，跨端多设备无缝协同。系统遵循分层设计：内核层 → 系统服务层 → 框架层 → 应用层，功能按“系统 → 子系统 → 功能/模块”逐级展开，支持按需裁剪 |
| **支持架构** | **ARM（ARMv7-A / V7A）** 。座舱芯片麒麟990A：4核泰山V120（华为自研超线程架构）+ 4核 ARM Cortex-A55 + Mali-G76 GPU + 达芬奇架构 NPU（2个D110大核 + 1个D100小核，NPU算力 3.5 TOPS）。麒麟 9610 车机模组基于标准化接口 |
| **硬件/芯片厂商** | 华为自研麒麟车机模组（990A、9610），适配高通、瑞萨等第三方车规级芯片 |
| **官方文档** | [华为开发者联盟——智能座舱 OEM 文档中心](https://developer.huawei.com/consumer/cn/overview/ICS) |
| **核心特点** | 全场景生态互通（手机、平板、车机），分布式能力领先，零层级桌面，“五界联盟”统一生态 |

**车企合作情况**：华为以 **“鸿蒙智行”五界联盟**（问界、智界、享界、尊界、尚界）为核心，覆盖赛力斯、奇瑞、北汽、江淮、上汽五大品牌。除联盟外，东风日产已推出全球首款搭载鸿蒙座舱的燃油车天籁·鸿蒙座舱（鸿蒙座舱 5.0），上汽通用五菱首款旗舰车型华境 S 全系标配华为乾崑智驾 + 鸿蒙座舱方案。广汽集团、比亚迪、长城汽车、长安阿维塔等多家车企均不同程度采用华为鸿蒙智能座舱方案。


### 3.2 斑马智行 —— AliOS

| 维度 | 内容 |
|------|------|
| **系统名称** | AliOS（自研智能汽车操作系统） |
| **开发主体** | 斑马智行（阿里巴巴持股 41.67%，上汽集团持股 32.9%） |
| **技术架构** | **全栈自研**，采用 **云端一体多核架构和分布异构融合框架**，支持微内核和宏内核及面向服务的架构（SOA）。三层架构：OS 内核 + AI 全栈 + 服务生态。跨平台能力：对底层异构芯片及硬件资源进行统一抽象与管理，是国内唯一实现多芯适配的车用 OS |
| **支持架构** | **ARM（ARMv9.2 全大核架构跨平台）** 。典型硬件：紫光展锐 A8880（ARM全大核）、芯驰科技 X10（ARMv9.2 CPU 架构，CPU性能 200K DMIPS，GPU 1800 GFLOPS，NPU 40 TOPS，内存带宽 154 GB/s） |
| **硬件/芯片厂商** | 适配主流车规级 SoC，包括紫光展锐、芯驰科技、高通、联发科、瑞萨、恩智浦（NXP）等，是国内唯一实现多芯适配的车用 OS |
| **官方文档** | [AliOS 官网](https://www.alios.cn) / [斑马智行官网](https://www.ebanma.com) |
| **核心特点** | 国内起步最早、量产规模最大的车用 OS，分层解耦合作模式，2021 年率先引入 AI 大模型技术，端云一体智能体系 |

**车企合作情况**：已合作上汽、一汽、南北大众等 10+ 个汽车品牌、40+ 款车型，累计覆盖超 100 万辆智能汽车。中国每 3 辆大众新车中就有 1 辆合作斑马智行。具体合作包括：**上汽集团**（荣威 RX5、智己汽车、MG、MAXUS，核心品牌全覆盖）、**大众系**（从独立座舱应用到 Powered by AliOS 再到全栈方案）、**宝马**（中国全系标配斑马语音助理，2026 年起新世代车型搭载斑马元神 AI 大模型助手）、**一汽红旗与现代汽车**（大模型座舱新体验）。


### 3.3 比亚迪 —— DiLink

| 维度 | 内容 |
|------|------|
| **系统名称** | DiLink（比亚迪自主研发的智能网联系统） |
| **开发主体** | 比亚迪股份有限公司 |
| **技术架构** | 基于 **Android 深度定制开发**，自主研发车载智能网联系统 |
| **支持架构** | **ARM** |
| **硬件/芯片厂商** | 适配高通骁龙系列车规级芯片，如 SM6350、SM7325 等 |
| **官方文档** | [比亚迪 DiLink 开发者平台](https://developer.byd.com) |
| **核心特点** | 横屏自适应、开放生态应用市场、智能语音交互、车辆远程控制、持续 OTA 升级 |

**车企合作情况**：DiLink 覆盖比亚迪旗下仰望、腾势、方程豹、王朝、海洋五大品牌。2025 年 12 月，比亚迪与火山引擎合作将豆包大模型融入 DiLink 系统，覆盖五大品牌全量在售车型。


### 3.4 蔚来 —— Banyan / Cedar

| 维度 | 内容 |
|------|------|
| **系统名称** | Banyan 榕（NT2 平台）、Cedar 雪松 / Cedar S（NT3 平台） |
| **开发主体** | 蔚来汽车 |
| **技术架构** | 基于 **Linux 自研**，搭载自研 NWM（NIO World Model）世界模型 —— 中国首个基于多元自回归架构的生成式具身驾驶模型，可在 100 毫秒内同步推演 216 种潜在行车场景 |
| **支持架构** | **ARM** |
| **硬件/芯片厂商** | 座舱：高通骁龙 8295（NT3 平台）/ 8155（NT2 平台）；智驾：英伟达 Orin‑X |
| **官方文档** | 蔚来官方 App 及官网提供系统更新日志和功能说明 |
| **核心特点** | 高算力硬件支撑（Banyan 平台智驾 + 座舱总算力达 1016 TOPS），OTA 高频迭代，生成式世界模型深度落地 |

**车企合作情况**：搭载于蔚来自有品牌全系车型。截至 2026 年 1 月，Banyan 系统已完成第 40 次 OTA 升级，覆盖逾 46 万辆已交付车辆。自研世界模型 NWM 已全量推送至 NT2 平台全系车型。


## 第四章 知名车企车载 OS 使用情况汇总

### 4.1 国内车企

| 车企 | 车载操作系统名称 | 技术来源 | 支持架构 | 核心特点 |
|------|-----------------|---------|---------|---------|
| **华为/鸿蒙智行联盟** | 鸿蒙座舱 HarmonySpace | 华为自研 | ARM | 微内核分布式，五界联盟统一生态 |
| **上汽集团** | AliOS | 斑马智行 | ARM | 多芯适配唯一，阿里深度赋能 |
| **一汽集团** | AliOS（红旗等） | 斑马智行 | ARM | 大模型座舱体验 |
| **比亚迪** | DiLink | 自研（Android 定制） | ARM | 豆包大模型上车，五大品牌全覆盖 |
| **蔚来** | Banyan / 雪松 | 自研（Linux + NWM） | ARM | 1016 TOPS 算力，生成式世界模型 |
| **吉利/领克/银河** | Flyme Auto | 亿咖通 + 魅族 | ARM | 跨终端融合，226 万台装机量 |
| **东风日产** | 鸿蒙座舱 | 华为合作 | ARM | 全球首款鸿蒙燃油车 |
| **上汽通用五菱** | 鸿蒙座舱 | 华为合作 | ARM | 华境 S 满血华为方案 |
| **奇瑞** | 鸿蒙智行（智界） | 华为合作 | ARM | 五界联盟成员 |
| **北汽** | 鸿蒙智行（享界） | 华为合作 | ARM | 五界联盟成员 |
| **江淮** | 鸿蒙智行（尊界） | 华为合作 | ARM | 五界联盟成员 |
| **赛力斯** | 鸿蒙智行（问界） | 华为合作 | ARM | 五界联盟成员 |

### 4.2 国际车企

| 车企 | 车载操作系统名称 | 技术来源 | 支持架构 | 核心特点 |
|------|-----------------|---------|---------|---------|
| **通用汽车** | RHIVOS / Ultifi 平台 | Red Hat 合作 / 自研 | ARM + x86‑64 | RHIVOS 首家合作伙伴，无需开发底层 OS |
| **特斯拉** | Tesla OS | 全栈自研（Linux） | x86（AMD APU） | 行业最早 OTA，软硬件垂直整合 |
| **奔驰** | MB.OS | 全栈自研 | ARM | 四大域统一，整合微软/谷歌 AI |
| **大众** | VW.OS | 自研 + QNX 底层 + 开放合作 | ARM | 从自研转向开放生态 |
| **沃尔沃** | Android Automotive OS | Google 合作 | ARM | 主要开发伙伴，率先搭载 Android 15 + Gemini |
| **通用汽车（主方案）** | Android Automotive + 自研 | Google 合作 + 自研 | ARM | 将移除 CarPlay 全面转向集成方案 |
| **丰田** | AGL + 自研 | AGL 开源 | x86 + ARM | IVI 全系搭载 AGL |
| **宝马** | BMW OS / 新世代操作系统 X | 自研 + AliOS 合作 | ARM | 70% 源代码中国本土开发 |
| **福特** | SYNC（Linux / Android 定制） | 混合架构 | ARM | IVI 采用 Linux + AGL |
| **雷诺 / 本田 / Stellantis** | Android Automotive OS | Google 合作 | ARM | 多款车型采用 |
| **现代 / 起亚** | 自研 ccOS + Android Automotive | 自研 + Google 合作 | ARM | 多层级组合方案 |


## 第五章 关键趋势与总结

### 5.1 架构趋势：ARM 主导车载计算，x86 保持差异化竞争力

车载操作系统领域呈现 **ARM 架构全面主导、x86 在高端场景保持竞争力** 的趋势：

- **ARM 架构**（ARMv7/v8/ARM64/AArch64）：移动端成熟生态向车规领域自然延伸，低功耗和高集成度特性完美适配“中央计算+区域控制器”的软件定义汽车架构。**QNX、Android Automotive OS、AGL、华为鸿蒙、斑马智行 AliOS、比亚迪 DiLink、蔚来 Banyan、MB.OS、VW.OS** 等系统均以 ARM 为主线。
- **x86/x86-64 架构**：以高性能计算能力见长，专注高端信息娱乐系统（IVI）和自动驾驶模型训练场景。**RHIVOS** 原生支持 x86-64 + ARM AArch64 双架构。**Tesla OS** 采用 AMD APU（x86-64）垂直整合路线，体现 x86 在高性能场景的差异化竞争力。
- **QEMU / 虚拟化**：AGL 和 Android Automotive 均利用 QEMU 实现跨架构开发和测试，降低硬件依赖。

### 5.2 安全域格局：QNX 仍为安全标杆，RHIVOS 成为 Linux 安全路线破局者

在功能安全要求最高的仪表、ADAS 与安全域中：
- **QNX** 凭借 ISO 26262 ASIL‑D 最高安全认证和成熟生态系统，稳居统治地位。
- **RHIVOS** 则开创了 Linux 车规级功能安全的新路径（ISO 26262 ASIL‑B 安全认证 + 混合关键性认证），为首家通过 Linux 功能安全认证的商业发行版厂商，并以“上游开源 + 下游安全认证”模式平衡了开源灵活性与安全合规性。随着 2025 年 Q3 量产发布，RHIVOS 有望成为继 QNX 之后安全域的第二大选择。
- **AGL** 通过容器技术和开源社区协作提供灵活的安全部署方案。

### 5.3 座舱与生态：Android Automotive 生态领先，国内联盟模式差异化竞争

- **Android Automotive OS** 凭借完整的 Google 服务生态、开发者生态和 HAL 硬件抽象层，在全球座舱市场快速扩张。沃尔沃、通用、福特等主流车企纷纷拥抱。
- **华为鸿蒙座舱（HarmonySpace）** 以“微内核 + 分布式 + 全场景”形成差异化竞争力，“五界联盟”打造统一标准。
- **斑马智行 AliOS** 秉持“分层解耦”开放理念，以多芯适配跨平台能力获得宝马、大众等品牌深度合作。
- **AGL** 以其开源无许可费用优势，获得丰田等车企 IVI 系统批量采用。

### 5.4 AI 大模型深度上车：从技术概念到全场景落地

AI 大模型已成为各家车载操作系统竞争的核心赛道之一：

- **RHIVOS** 明确了“软件优先”开发范式，支持 AI 模型在车辆中的高效部署和持续更新。
- **斑马智行 AliOS** 率先在 2021 年引入 AI 大模型技术，旗下元神 AIOS 具备跨平台、跨模型能力，加速大模型上车进程。
- **华为鸿蒙** 深度融合盘古大模型，支持端云协同 AI 能力。
- **比亚迪 DiLink** 联合火山引擎将豆包大模型融入五大品牌全量车型。
- **蔚来** 自主研发的 NWM 世界模型已全量推送 NT2 平台，展现生成式模型与智驾融合深度落地。

### 5.5 国内 vs 国际：两种模式，两种生态

| 维度 | 国内 | 国际 |
|------|------|------|
| **主流方案** | 华为鸿蒙生态 + AliOS 对外授权 + 车企自研 | QNX（安全域统治级）+ Android Automotive + 车企自研（Tesla、MB.OS） |
| **架构偏好** | ARM 为主，华为自研泰山核心 | ARM（QNX/Android）+ x86（Tesla/RHIVOS） |
| **AI 大模型渗透** | 豆包大模型（比亚迪）、NWM 世界模型（蔚来）、盘古大模型（华为）、元神 AI（斑马）全面落地 | Gemini（沃尔沃 Android 15）、ChatGPT/Gemini（奔驰） |
| **生态构建模式** | “联盟制”（华为五界联盟）+ “分层解耦”（AliOS）+ 独立自研 | 安全域 QNX + 座舱域 Android Automotive/自研 |


## 附录：官方文档汇总表

| 操作系统 | 官方文档入口 |
|---------|------------|
| BlackBerry QNX | [qnx.com](https://www.qnx.com) / [QNX BSP Library](https://qnx.software/en/developers/get-started/board-support-packages) |
| Android Automotive OS | [Android Developers - Automotive](https://developer.android.com/training/cars) / [AOSP Automotive](https://source.android.com/docs/automotive) |
| AGL | [docs.automotivelinux.org](https://docs.automotivelinux.org) / [AGL 官网](https://www.automotivelinux.org) |
| **RHIVOS（红帽）** | [Official RHIVOS Data Sheet](https://www.redhat.com/en/resources/in-vehicle-operating-system-datasheet) / [AutoSD GitHub/Community](https://sigs.centos.org/automotive/) / [AutoSD Hardware Enablement](https://sigs.centos.org/automotive/autosd-10/hardware-enablement/index.html) |
| 华为鸿蒙座舱 | [华为开发者联盟——智能座舱 OEM 文档中心](https://developer.huawei.com/consumer/cn/overview/ICS) |
| 斑马智行 AliOS | [AliOS 官网](https://www.alios.cn) / [斑马智行官网](https://www.ebanma.com) |
| 比亚迪 DiLink | [比亚迪 DiLink 开发者平台](https://developer.byd.com) |
| Tesla OS | Tesla 官网 / GitHub |
| Mercedes-Benz MB.OS | Mercedes-Benz 官网 |
| Volkswagen VW.OS | CARIAD 官网 |

> **报告编制说明：** 本报告数据截至 2026 年 5 月，各系统官方文档链接均为公开可访问入口。RHIVOS 计划于 2025 年 Q3 正式量产发布，当前数据基于官方公开资料及合作伙伴公告。
