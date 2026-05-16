---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
- /about/
- /about.html
---

<style>
dl {
margin-bottom: 60px; /* 调整这个值以获得合适的间距 */
clear: both;
}

/* 全局文本颜色 */
body {
color: #333; /* 主要文本颜色 */
background-image: url('../images/bg.jpg'); /* 背景图片 */
background-size: cover;
background-position: center;
background-attachment: fixed;
}

/* 链接颜色 */
a {
color: #0066cc; /* 链接颜色 */
}

/* 作者名字颜色 */
strong {
color: #000; /* 作者名字颜色 */
}

/* 年份标题颜色 */
.year-title {
color: #666;
}

/* 会议标签样式 */
.conference-label {
position: absolute;
top: 10px;
left: -5px;
background-color: #2c3e50;  /* 深蓝色背景 */
color: white;  /* 白色文字 */
padding: 6px 12px;
border-radius: 6px;
font-size: 0.95em;
font-weight: 600;
letter-spacing: 0.5px;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
z-index: 1;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
font-style: italic;  /* 添加斜体 */
}

/* 鼠标悬停效果 */
.conference-label:hover {
background-color: #34495e;  /* 悬停时稍微变亮 */
transition: background-color 0.2s ease;
}

dl dt img {
width: 100%; /* 在移动端默认占满宽度 */
aspect-ratio: 2/1; /* 设置宽高比为2:1，即高度为宽度的一半 */
object-fit: cover; /* 确保图片不会被裁剪 */
display: block;
margin: 10px 10px 10px 0px; /* 适当的间距 */

/* 添加美化效果 */
border-radius: 8px; /* 让图片有轻微的圆角 */
border: 2px solid #ddd; /* 添加淡灰色的边框 */
box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); /* 添加轻微阴影 */
padding: 5px; /* 给图片一些内边距，让它不贴着边框 */
background-color: #fff; /* 设置背景色，让图片更加干净 */
}

/* 在桌面端（宽度大于768px）时固定宽度 */
@media screen and (min-width: 768px) {
dl dt img {
width: 350px;
}
}

dl dt {
position: relative;
}

hr {
border: 1px solid #ebebeb; /* 调整分隔线的颜色和样式 */
/* margin: 10px;  */
clear: both; 
}

dl dd {
margin-top: 5px; 
margin-bottom: 5px;
}

dl dd strong {
font-weight: bold;
color: black;
}

.co-first {
color: red;
}

.down {
transform: rotate(180deg);
}

/* 教育和工作经历卡片样式 */
.experience-card, .education-card {
display: flex;
align-items: center;
gap: 25px;
margin-bottom: 30px;
padding: 20px;
background: #f8f9fa;
border-radius: 12px;
transition: all 0.3s ease;
border: 1px solid #e9ecef;
}

.experience-card:hover, .education-card:hover {
transform: translateY(-3px);
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
border-color: #dee2e6;
}

.experience-info, .education-info {
flex: 1;
}

.experience-logo, .education-logo {
flex-shrink: 0;
width: 100px;
height: 100px;
display: flex;
align-items: center;
justify-content: center;
background: white;
border-radius: 10px;
padding: 10px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.experience-logo img, .education-logo img {
width: 100%;
height: 100%;
object-fit: contain;
}

.experience-title, .education-title {
font-size: 1.2em;
margin-bottom: 8px;
color: #2c3e50;
}

.experience-title a, .education-title a {
color: #2c3e50;
text-decoration: none;
transition: color 0.3s ease;
}

.experience-title a:hover, .education-title a:hover {
color: #3498db;
}

.experience-role, .education-role {
color: #666;
font-style: italic;
margin-bottom: 5px;
}

.experience-topics, .education-topics {
color: #666;
font-style: italic;
}

.section-title {
font-size: 1.8em;
color: #2c3e50;
margin: 40px 0 20px;
padding-bottom: 10px;
border-bottom: 2px solid #ecf0f1;
}

/* 奖学金和荣誉部分样式 */
.honors-list {
list-style: none;
padding: 0;
}

.honors-list li {
margin-bottom: 15px;
padding: 15px 20px;
background: #f8f9fa;
border-radius: 8px;
border-left: 4px solid #3498db;
transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.honors-list li:hover {
transform: translateX(5px);
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.honors-list li strong {
color: #2c3e50;
}

.honors-list li a {
color: #3498db;
text-decoration: none;
transition: color 0.3s ease;
}

.honors-list li a:hover {
color: #2980b9;
}

/* 服务部分样式 */
.service-section {
margin-bottom: 30px;
}

.service-section h3 {
color: #2c3e50;
font-size: 1.3em;
margin: 25px 0 15px;
padding-bottom: 8px;
border-bottom: 2px solid #ecf0f1;
}

.service-list {
list-style: none;
padding: 0;
}

.service-list li {
margin-bottom: 12px;
padding: 12px 15px;
background: #f8f9fa;
border-radius: 6px;
transition: transform 0.3s ease;
}

.service-list li:hover {
transform: translateX(5px);
}

.service-list li a {
color: #3498db;
text-decoration: none;
transition: color 0.3s ease;
}

.service-list li a:hover {
color: #2980b9;
}
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# About
I am a  Ph.D. candidate majoring in Software Engineering at School of Computer Science and Artificial Intelligence, Zhengzhou University. My research interests include data mining and machine learning, with a particular focus on recommender systems, graph representation learning, and information bottleneck. I have published and co-authored some research papers in several top journals and conferences.

<!-- I am currently an PhD Student from the University of Hong Kong. My research interests include Recommendation, Graph Learning, Multimodal Understanding, and Data Privacy.

I have extensive research experience and a strong publication record in multimodal recommendation, collaborative filtering, group recommendation, and graph generalization. I have also explored multimodal understanding and the application of graph-based methods to downstream tasks, with several publications in these areas. Currently, I am actively pursuing new directions in reasoning-aware recommendation, agentic recommendation, and graph for scientific discovery.-->

I look forward to collaborating in the field of Recommendation and Graph Learning.

I am also seeking self-motivated collaborators.

Feel free to contact me via <a href="mailto:qiangguo@zzu.edu.cn">Email</a> or <a href="https://Jinfeng-Xu.github.io/images/WeChat.jpeg">WeChat</a>. 

<!-- 📄 You can download my CV <a href="assets/徐锦峰-CV.pdf" style="color: #0066cc; text-decoration: underline;" target="_blank">here</a>.-->

<!-- <div style="background: linear-gradient(135deg, #f3f8ff, #e8f4fd); padding: 20px; border-radius: 10px; margin: 20px 0; border: 2px solid #1976d2; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); position: relative; overflow: hidden;">
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.3)); pointer-events: none;"></div>
<p style="margin: 0; position: relative; z-index: 1;"> <strong style="color: red">🌟 📢 PostDoc Opportunity</strong><br>
I am looking for PostDoc opportunities in 26Fall related to Recommendation and Graph Learning, especially in labs based in the United States/Hong Kong/Singapore. My research interests include Recommendation System, Data Privacy, Graph Learning, Self-supervised Learning, Computer Vision, and Federated Learning. If our research interests align, please feel free to contact me via <a href="mailto:jinfeng@connect.hku.hk">Email</a> or <a href="https://Jinfeng-Xu.github.io/images/WeChat.jpeg">WeChat</a>.
</p>
</div>-->
<hr>
# 🔥 News

<div style="max-height: 350px; overflow-y: auto; padding: 20px; background: #f8f9fa; border-left: 4px solid #2c3e50; margin: 0px 0;">
<style>
/* 为 Webkit 浏览器（Chrome, Safari, Edge）设置滚动条样式 */
div::-webkit-scrollbar {
width: 8px;
}

div::-webkit-scrollbar-track {
background: #e9ecef;
border-radius: 4px;
}

div::-webkit-scrollbar-thumb {
background: #2c3e50;
border-radius: 4px;
}

div::-webkit-scrollbar-thumb:hover {
background: #1a252f;
}

/* 为 Firefox 设置滚动条样式 */
div {
scrollbar-width: thin;
scrollbar-color: #2c3e50 #e9ecef;
}
</style>

<ul style="list-style-type: none; padding-left: 0; margin: 0;">
<li><em>2025.05:</em> 🎉 One paper on knowledge-aware recommendation has been accepted by <strong>Expert Systems with Applications (ESWA)</strong>. </li>
<li><em>2025.07:</em> 🎉 One collaborative paper has been accepted by <strong>ACM MM 2025</strong>. Congratulations to <strong>Haichuan Fang</strong>! </li>
<li><em>2025.05:</em> 🎉 One collaborative paper has been accepted by <strong>Knowledge-Based Systems (KBS)</strong>. Congratulations to <strong>Yiqiang Mao</strong>! </li>
<li><em>2025.03:</em> 🎉 One paper on knowledge-aware recommendation has been accepted by <strong>Information Processing & Management (IPM)</strong>. </li>  
<li><em>2024.12:</em> 🎉 One collaborative paper (co-corresponding author) has been accepted by <strong>IEEE Transactions on Industrial Informatics (TII)</strong>. Congratulations to <strong>Yiqiang Mao</strong>! </li>

<!--
 <li><em>2026.04:</em> 🎉 One conference extension paper on mutlimodal recommendation has been accepted by <strong>ACM Transactions on Recommender Systems (TORS)</strong>. </li>
<li><em>2026.03:</em> 🎉 One paper supervised by me as the corresponding author has been accepted by <strong>CVPR 2026 (findings)</strong>. Congratulations to <strong>Ge Wang</strong>! </li>
<li><em>2026.03:</em> 📚️ I serve as a reviewer for <strong>Neural Networks (NEUNET)</strong>. </li>
<li><em>2026.03:</em> 📚️ I serve as a reviewer for <strong>Expert Systems With Applications (ESWA)</strong>. </li>
<li><em>2026.03:</em> 📚️ I serve as a reviewer for <strong>ACM MM 2026</strong>. </li>
<li><em>2026.03:</em> 📚️ I serve as a reviewer for <strong>ECCV 2026</strong>. </li>
<li><em>2026.03:</em> 📚️ I serve as a reviewer for <strong>IEEE Transactions on Big Data (TBD)</strong>. </li>
<li><em>2026.02:</em> 🎉 One paper on mutlimodal sequential recommendation has been accepted by <strong>ICDE 2026</strong>. </li>
<li><em>2026.02:</em> 📚️ I serve as a PC member for <strong>ICMR 2026</strong>. </li>
<li><em>2026.02:</em> 📚️ I serve as a PC member for <strong>SIGIR 2026</strong>. </li>
<li><em>2026.01:</em> 📚️ I serve as a reviewer for <strong>KDD 2026 (Cycle 2)</strong>. </li>
<li><em>2026.01:</em> 🎉 Two collaborative papers have been accepted by <strong>ICLR 2026</strong>. Congratulations to <strong>Jinze Li</strong> and <strong>Jianheng Tang</strong>! </li>
<li><em>2026.01:</em> 📚️ I serve as a reviewer for <strong>ICML 2026</strong>. </li>
<li><em>2026.01:</em> 📚️ I serve as a reviewer for <strong>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)</strong>. </li>
<li><em>2025.12:</em> 📚️ I serve as a reviewer for <strong>Information Processing and Management (IPM)</strong>. </li>
<li><em>2025.12:</em> 🎉 One paper on group recommendation has been accepted by <strong>ACM Transactions on Information Systems (TOIS)</strong>. </li>
<li><em>2025.11:</em> 📚️ I serve as a reviewer for <strong>Neurocomputing (NEUCOM)</strong>. </li>
<li><em>2025.11:</em> 📚️ I serve as a reviewer for <strong>Pattern Recognition (PR)</strong>. </li>
<li><em>2025.11:</em> 🎉 Two papers on universal graph prompt tuning and mutlimodal recommendation have been accepted by <strong>KDD 2026</strong>. </li>
<li><em>2025.11:</em> 📚️ I serve as a reviewer for <strong>Kwowledge-Based System (KBS)</strong>. </li>
<li><em>2025.11:</em> 📚️ I serve as a reviewer for <strong>IEEE Wireless Communications (IEEE WCM)</strong>. </li>
<li><em>2025.11:</em> 📚️ I serve as a reviewer for <strong>WWW 2026 (Full, Short, Web4Good Tracks)</strong>. </li>
<li><em>2025.11:</em> 🎈 Honored to provide a presentation seminar at Hanyang University. Grateful to <strong>Prof. Sang-Wook Kim</strong> for the invitation! </li>
<li><em>2025.11:</em> 🎉 One paper on multimodal personalized clustering has been accepted by <strong>AAAI 2026</strong>. </li>
<li><em>2025.10:</em> 📚️ I serve as a reviewer for <strong>ICLR 2026</strong>. </li>
<li><em>2025.10:</em> 📚️ I serve as a reviewer for <strong>ACM Transactions on Knowledge Discovery from Data (ACM TKDD)</strong>. </li>
<li><em>2025.10:</em> 📚️ I serve as a reviewer for <strong>ACM Transactions on Internet Technology (ACM TOIT)</strong>. </li>
<li><em>2025.10:</em> 🌐 My new personal academic homepage is now online.</li>
<li><em>2023.09-2025.10:</em> 🎈 I have published more than 10 papers in top-tier conferences and journals as the first author, including 1 KDD, 2 SIGIR, 1 ACM MM, 1 RecSys (Spotlight Oral), 3 CIKM, 1 AAAI, 1 ICASSP, 1 TKDE, 1 TOIS, 1 TMM, and 1 Information Fusion. </li>
<li><em>2023.09-2025.10:</em> 🎈 I have also contributed as a co-author to many outstanding works, including NDSS, TDSC, KDD, IROS (Oral), etc. </li>
<li><em>2023.09-2025.10:</em> 📚️ I have served as a reviewer for over 10 top-tier conferences (e.g., ICLR, NeurIPS, KDD, SIGIR, etc.) and 5 top-tier journals (e.g., TKDE, TOIS, TII, TIT, etc.). Additionally, I was honored as an Outstanding Reviewer and invited as a Session Chair at KDD 2025. </li>-->






</ul>
</div>

<br/>

<hr>
# 📝 Selected Publications ([Full List](https://scholar.google.com/citations?user=CpUZV-cAAAAJ&hl=en))
**# indicates the authors with equal contributions, and * indicates the corresponding authors.**

<dl>
<!-- <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/SG-URInit.png">
<span class="conference-label">IPM 2025</span>
</dt> -->
<dd><a href="https://www.sciencedirect.com/science/article/abs/pii/S030645732400339X"><strong>DCIB: Dual contrastive information bottleneck for knowledge-aware recommendation</strong></a></dd>
<dd><strong>Qiang Guo</strong>, Jialong Hai, Zhongchuan Sun, Bin Wu, Yangdong Ye![](http://latex.codecogs.com/svg.latex?\ast)</dd>
<dd> Information Processing & Management, 2025. (中科院1区 SCI, IF: 7.4)</dd>
</dl>


<dl>
<dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/CAMMSR.png">
<span class="conference-label">ICDE 2026</span>
</dt>
<dd><a href="https://arxiv.org/pdf/2603.04320"><strong>CAMMSR: Category-Guided Attentive Mixture of Experts for Multimodal Sequential Recommendation</strong></a></dd>
<dd><strong>Jinfeng Xu</strong>, Zheyu Chen, Shuo Yang, Jinze Li, Hewei Wang, Yijie Li, Jianheng Tang, Yunhuai Liu, and Edith Ngai</dd>
<dd> IEEE International Conference on Data Engineering (<strong>ICDE</strong>), 2026</dd>
</dl>


<hr>

<dl>
<dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/DGGVAE.png">
<span class="conference-label">TOIS 2026</span>
</dt>
<dd><a href="https://dl.acm.org/doi/pdf/10.1145/3785145"><strong>DGGVAE: Dual-Granularity Graph Variational Auto-Encoder for Group Recommendation</strong></a></dd>
<dd><strong>Jinfeng Xu</strong>, Zheyu Chen, Jinze Li, Shuo Yang, Wei Wang, Hewei Wang, Yijie Li, Xiping Hu, and Edith Ngai</dd>
<dd> ACM Transactions on Information Systems (<strong>TOIS</strong>), 2026</dd>
</dl>


<hr>

<dl>
<dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/LEAP.png">
<span class="conference-label">KDD 2026</span>
</dt>
<dd><a href="https://arxiv.org/pdf/2512.08763"><strong>Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning</strong></a></dd>
<dd><strong>Jinfeng Xu</strong>, Zheyu Chen, Shuo Yang, Jinze Li, Hewei Wang, Yijie Li, and Edith Ngai</dd>
<dd> ACM SIGKDD Conference on Knowledge Discovery and Data Mining (<strong>KDD</strong>), 2026</dd>
</dl>


<hr>

<dl>
<dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/VI-MMRec.png">
<span class="conference-label">KDD 2026</span>
</dt>
<dd><a href="https://arxiv.org/pdf/2512.08702"><strong>VI-MMRec: Similarity-Aware Training Cost-free Virtual User-Item Interactions for Multimodal Recommendation</strong></a></dd>
<dd><strong>Jinfeng Xu</strong>, Zheyu Chen, Shuo Yang, Jinze Li, Zitong Wan, Hewei Wang, Weijie Liu, Yijie Li, and Edith Ngai</dd>
<dd> ACM SIGKDD Conference on Knowledge Discovery and Data Mining (<strong>KDD</strong>), 2026</dd>
</dl>


<hr>
# 🎖 Honors and Awards
- 
<hr>
# 📖 Academic Background
- **Sep 2021 - Now:** Zhengzhou University (Ph.D. Candidate), Software Engineering <br>supervised by [Prof. Yangdong Ye](http://www5.zzu.edu.cn/mlis/)
- **Sep 2018 - Jun 2021:** Zhengzhou University (MSc), Software Engineering <br>supervised by [Prof. Yangdong Ye](http://www5.zzu.edu.cn/mlis/)
- **Sep 2010 - Jun 2014:** Shenzhen University (BSc), Computer Science and Technology
# 📖 Educations
<div class="education-card">
<div class="education-info">
<div class="education-title">
 <strong>2023.09 - 2026.07 (Expected)</strong><br/>
 PhD, University of Hong Kong
</div>
</div>
<div class="education-logo">
<img src="../images/HKU-logo.png" alt="University of Hong Kong" />
</div>
</div> 
<hr>
