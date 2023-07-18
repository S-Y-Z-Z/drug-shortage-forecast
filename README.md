<!--
 * @Author: callus
 * @Date: 2023-07-18 13:53:48
 * @LastEditors: callus
 * @Description: some description
 * @FilePath: /drug-shortage-forecast/README.md
-->
# drug-shortage-forecast
这是一个用来预测药品销售和库存的项目，主要是为了使用机器学习的相关内容来做一些事情

# ERROR: Could not build wheels for fbprophet, pystan, which is required to install pyproject.toml-based projects这个包装不上，所以fbprophet也装不上，估计还是版本的问题，但是不知道适配哪个版本，明天再说

# 需要安装fbprophet库 的几个代码都无法跑，需要安装的额外依赖根本装不上，官方给的解决办法没看懂，暂时放弃
已经从GitHub上把fbprophet 压缩包下载下来了，依据官方的推荐，执行这些命令就能安装

git clone https://github.com/facebook/prophet.git
cd prophet/python
python -m pip install -e .