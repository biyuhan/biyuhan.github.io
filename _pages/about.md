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
  :root {
    --homepage-text: #333;
    --homepage-primary: #2c3e50;
    --homepage-link: #0066cc;
    --homepage-muted: #666;
    --homepage-bg: #f8f9fa;
    --homepage-border: #e9ecef;
    --homepage-accent: #3498db;
    --homepage-body-size: 1.2em;
  }

  body {
    color: var(--homepage-text);
    background-image: url("{{ '/images/bg.jpg' | relative_url }}");
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
  }

  a {
    color: var(--homepage-link);
  }

  strong {
    color: #000;
  }

  hr {
    clear: both;
    border: 1px solid #ebebeb;
  }

  .page__content > p,
  .publication-note,
  .publication-list dd,
  .news-list li,
  .content-list li,
  .useful-links li,
  .info-card,
  .service-list li {
    font-size: var(--homepage-body-size);
    line-height: 1.6;
  }

  .page__content > p {
    margin-bottom: 1em;
  }

  .year-title {
    color: var(--homepage-muted);
  }

  .conference-label {
    position: absolute;
    top: 10px;
    left: -5px;
    z-index: 1;
    padding: 6px 12px;
    color: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 1.2em;
    font-style: italic;
    font-weight: 600;
    letter-spacing: 0.5px;
    background-color: var(--homepage-primary);
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }

  .conference-label:hover {
    background-color: #34495e;
    transition: background-color 0.2s ease;
  }

  .publication-list {
    clear: both;
    margin-bottom: 40px;
  }

  .publication-list dt {
    position: relative;
  }

  .publication-list dt img {
    display: block;
    width: 100%;
    margin: 10px 10px 10px 0;
    padding: 5px;
    aspect-ratio: 2 / 1;
    object-fit: cover;
    background-color: #fff;
    border: 2px solid #ddd;
    border-radius: 8px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  }

  .publication-list dd {
    margin-top: 5px;
    margin-bottom: 5px;
  }

  .publication-list dd strong {
    font-weight: 700;
  }

  @media screen and (min-width: 768px) {
    .publication-list dt img {
      width: 350px;
    }
  }

  .news-box {
    max-height: 350px;
    margin: 0;
    padding: 20px;
    overflow-y: auto;
    background: var(--homepage-bg);
    border-left: 4px solid var(--homepage-primary);
  }

  .news-box::-webkit-scrollbar {
    width: 8px;
  }

  .news-box::-webkit-scrollbar-track {
    background: var(--homepage-border);
    border-radius: 4px;
  }

  .news-box::-webkit-scrollbar-thumb {
    background: var(--homepage-primary);
    border-radius: 4px;
  }

  .news-box::-webkit-scrollbar-thumb:hover {
    background: #1a252f;
  }

  .news-box {
    scrollbar-color: var(--homepage-primary) var(--homepage-border);
    scrollbar-width: thin;
  }

  .news-list,
  .content-list,
  .service-list,
  .useful-links {
    padding-left: 0;
    list-style: none;
  }

  .news-list {
    margin: 0;
  }

  .news-list li {
    margin-bottom: 0.6em;
  }

  .content-list li,
  .service-list li {
    margin-bottom: 15px;
    padding: 15px 20px;
    background: var(--homepage-bg);
    border-left: 4px solid var(--homepage-accent);
    border-radius: 8px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .content-list li:hover,
  .service-list li:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .content-list li strong,
  .service-list li strong {
    color: var(--homepage-primary);
  }

  .content-list li a,
  .service-list li a,
  .useful-links li a {
    color: var(--homepage-accent);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .content-list li a:hover,
  .service-list li a:hover,
  .useful-links li a:hover {
    color: #2980b9;
  }

  .info-card {
    margin-bottom: 20px;
    padding: 18px 20px;
    background: var(--homepage-bg);
    border: 1px solid var(--homepage-border);
    border-left: 4px solid var(--homepage-primary);
    border-radius: 10px;
  }

  .info-card p:last-child,
  .info-card ul:last-child {
    margin-bottom: 0;
  }

  .info-card ul {
    margin-top: 8px;
  }

  .subsection-title {
    margin: 24px 0 12px;
    color: var(--homepage-primary);
    font-size: 1.25em;
    font-weight: 700;
  }

  .education-card,
  .experience-card {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-bottom: 30px;
    padding: 20px;
    background: var(--homepage-bg);
    border: 1px solid var(--homepage-border);
    border-radius: 12px;
    transition: all 0.3s ease;
  }

  .education-card:hover,
  .experience-card:hover {
    transform: translateY(-3px);
    border-color: #dee2e6;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  }

  .education-info,
  .experience-info {
    flex: 1;
  }

  .education-logo,
  .experience-logo {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: center;
    width: 100px;
    height: 100px;
    padding: 10px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .education-logo img,
  .experience-logo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .education-title,
  .experience-title {
    margin-bottom: 8px;
    color: var(--homepage-primary);
    font-size: var(--homepage-body-size);
  }

  .education-title a,
  .experience-title a {
    color: var(--homepage-primary);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .education-title a:hover,
  .experience-title a:hover {
    color: var(--homepage-accent);
  }

  .education-role,
  .education-topics,
  .experience-role,
  .experience-topics {
    color: var(--homepage-muted);
    font-style: italic;
  }

  .education-role,
  .experience-role {
    margin-bottom: 5px;
  }

  @media screen and (max-width: 600px) {
    .education-card,
    .experience-card {
      align-items: flex-start;
      gap: 16px;
      padding: 16px;
    }

    .education-logo,
    .experience-logo {
      width: 72px;
      height: 72px;
    }
  }
</style>

<span class="anchor" id="about-me"></span>
# About Me

I am currently a faculty member in the School of Computer Science and Artificial Intelligence at Zhengzhou University. I received my Ph.D. degree in Software Engineering from Zhengzhou University in June 2025, under the supervision of <a href="http://www5.zzu.edu.cn/mlis/"><strong>Prof. Yangdong Ye</strong></a>.

My research interests lie broadly in data mining and machine learning, with a particular focus on recommender systems, multimodal learning, information bottleneck, and graph representation learning. My research aims to develop effective, robust, and interpretable learning methods for recommendation and graph-based data analysis. I have published and co-authored several papers in peer-reviewed journals and conferences in related areas.

I am expected to recruit master’s students in the next admission cycle. Prospective students who are interested in recommender systems, multimodal learning, graph learning, information bottleneck, and related topics are warmly encouraged to contact me.

I also welcome academic discussions and potential collaborations with researchers working in related fields.

Official homepage is <a href="https://www7.zzu.edu.cn/csai/info/1233/3668.htm">here</a>. Feel free to contact me via <a href="mailto:qiangguo@zzu.edu.cn">Email</a> or <a href="{{ '/images/wechat.png' | relative_url }}">WeChat</a>.

<hr>

<span class="anchor" id="news"></span>
# 🔥 News

<div class="news-box">
  <ul class="news-list">
    <li><em>2025.12:</em> 🎉 One paper on knowledge-aware recommendation has been accepted by <strong>Expert Systems with Applications (ESWA)</strong>.</li>
    <li><em>2025.07:</em> 🎉 One collaborative paper has been accepted by <strong>ACM MM 2025</strong>. Congratulations to <strong>Haichuan Fang</strong>!</li>
    <li><em>2025.05:</em> 🎉 One collaborative paper has been accepted by <strong>Knowledge-Based Systems (KBS)</strong>. Congratulations to <strong>Yiqiang Mao</strong>!</li>
    <li><em>2025.03:</em> 🎉 One paper on knowledge-aware recommendation has been accepted by <strong>Information Processing &amp; Management (IPM)</strong>.</li>
    <li><em>2024.12:</em> 🎉 One collaborative paper (co-corresponding author) has been accepted by <strong>IEEE Transactions on Industrial Informatics (TII)</strong>. Congratulations to <strong>Yiqiang Mao</strong>!</li>
  </ul>
</div>

<br>
<hr>

<span class="anchor" id="publications"></span>
# 📝 Selected Publications ([Full List](https://scholar.google.com/citations?user=CpUZV-cAAAAJ&hl=en))

<p class="publication-note"><strong># indicates the authors with equal contributions, and * indicates the corresponding authors.</strong></p>

<dl class="publication-list">
  <dd><a href="https://www.sciencedirect.com/science/article/pii/S0957417425022912"><strong>Knowledge-refined information bottleneck for contrastive recommendation</strong></a></dd>
  <dd><strong>Qiang Guo</strong>, Bin Wu, Zhongchuan Sun, Haichuan Fang, Yangdong Ye*</dd>
  <dd>Expert Systems with Applications, 2025. (中科院1区 SCI, IF: 7.5)</dd>
</dl>

<dl class="publication-list">
  <dd><a href="https://www.sciencedirect.com/science/article/abs/pii/S030645732400339X"><strong>DCIB: Dual contrastive information bottleneck for knowledge-aware recommendation</strong></a></dd>
  <dd><strong>Qiang Guo</strong>, Jialong Hai, Zhongchuan Sun, Bin Wu, Yangdong Ye*</dd>
  <dd>Information Processing &amp; Management, 2025. (中科院1区 SCI, IF: 7.4)</dd>
</dl>

<dl class="publication-list">
  <dd><a href="https://link.springer.com/article/10.1007/s40747-024-01427-x"><strong>Consistency-constrained RGB-T crowd counting via mutual information maximization</strong></a></dd>
  <dd><strong>Qiang Guo</strong>, Pengcheng Yuan, Xiangming Huang, Yangdong Ye*</dd>
  <dd>Complex &amp; Intelligent Systems, 2024. (中科院2区 SCI, IF: 5.0)</dd>
</dl>

<dl class="publication-list">
  <dd><a href="https://www.sciencedirect.com/science/article/abs/pii/S0950705120308200"><strong>Learning a deep network with cross-hierarchy aggregation for crowd counting</strong></a></dd>
  <dd><strong>Qiang Guo</strong>, Xin Zeng, Shizhe Hu, Sonephet Phoummixay, Yangdong Ye*</dd>
  <dd>Knowledge-Based Systems, 2021. (中科院1区 SCI, IF: 8.1)</dd>
</dl>

<hr>

<span class="anchor" id="funding"></span>
# 💰 Funding

<ul class="content-list">
  <li>To be updated.</li>
</ul>

<hr>

<span class="anchor" id="honors"></span>
# 🎖 Honors

<ul class="content-list">
  <li>To be updated.</li>
</ul>

<hr>

<span class="anchor" id="education"></span>
# 📖 Education

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2021.09 - 2025.06:</strong><br>
      Zhengzhou University (PhD), Software Engineering supervised by <a href="http://www5.zzu.edu.cn/mlis/"><strong>Prof. Yangdong Ye</strong></a>
    </div>
  </div>
  <div class="education-logo">
    <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University">
  </div>
</div>

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2018.09 - 2021.06:</strong><br>
      Zhengzhou University (MSc), Computer Science and Technology supervised by <a href="http://www5.zzu.edu.cn/mlis/"><strong>Prof. Yangdong Ye</strong></a>
    </div>
  </div>
  <div class="education-logo">
    <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University">
  </div>
</div>

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2010.09 - 2014.06:</strong><br>
      Shenzhen University (BSc), Software Engineering
    </div>
  </div>
  <div class="education-logo">
    <img src="{{ '/images/szulogo.png' | relative_url }}" alt="Shenzhen University">
  </div>
</div>

<hr>

<span class="anchor" id="courses"></span>
# 👨‍🏫 Courses

<div class="info-card">
  <p>Teaching information will be updated as courses are finalized.</p>
  <!-- Example:
  <ul>
    <li><strong>Course Name</strong>, Undergraduate/Graduate, Zhengzhou University, Semester.</li>
  </ul>
  -->
</div>

<hr>

<span class="anchor" id="students"></span>
# 🎓 Students

<div class="info-card">
  <p>I am expected to recruit master’s students in the next admission cycle. Students interested in recommender systems, multimodal learning, graph representation learning, information bottleneck, and related machine learning topics are welcome to contact me.</p>
  <p>Please include your CV, transcript, research interests, and any representative projects or publications when contacting me.</p>
</div>

<hr>

<span class="anchor" id="service"></span>
# 🤝 Service

<div class="service-section">
  <h3 class="subsection-title">Reviewer / Program Committee</h3>
  <ul class="service-list">
    <li>To be updated.</li>
  </ul>
</div>

<div class="service-section">
  <h3 class="subsection-title">Editorial Service</h3>
  <ul class="service-list">
    <li>To be updated.</li>
  </ul>
</div>

<div class="service-section">
  <h3 class="subsection-title">Professional Service</h3>
  <ul class="service-list">
    <li>To be updated.</li>
  </ul>
</div>

<hr>

<span class="anchor" id="useful-links"></span>
# 🔗 Useful Links

<ul class="useful-links">
  <li><strong>CCF List:</strong> <a href="https://ccf.atom.im/">ccf.atom.im</a></li>
  <li><strong>CCF Deadlines:</strong> <a href="https://ccfddl.com/">CCF Deadlines</a></li>
  <li><strong>AI Deadlines:</strong> <a href="https://aideadlin.es/?sub=ML,CV,CG,NLP,RO,SP,DM,AP,KR,HCI">AI Conference Deadlines</a></li>
  <li><strong>CSRankings:</strong> <a href="https://csrankings.org/">Computer Science Rankings</a></li>
  <li><strong>Core Ranking:</strong> <a href="https://portal.core.edu.au/conf-ranks/">Conference Portal</a></li>
</ul>

<hr>
