# puzzle-recognize
基于pillow 实现的滑块验证码识别

# 实现
1. 使用pillow将底图、滑块图处理成黑白
2. 用滑块轮廓最清晰的一段曲线逐像素去匹配同高度的底图
