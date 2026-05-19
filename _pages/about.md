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
  /* =========================================================
     1. Global design variables
     修改字体、字号、颜色、卡片间距时，优先调整这里的变量。
     ========================================================= */
  :root {
    --homepage-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", "Source Han Sans SC", sans-serif;
    --homepage-text: #333;
    --homepage-primary: #2c3e50;
    --homepage-link: #0066cc;
    --homepage-bg: #f8f9fa;
    --homepage-border: #e9ecef;
    --homepage-accent: #3498db;
    --homepage-card-hover-border: #dee2e6;

    /* 正文字号：电脑端正文调整为接近手机端的舒适大小 */
    --homepage-content-size: 16px;
    --homepage-body-size: 1.08em;
    --homepage-mobile-content-size: 15.5px;
    --homepage-mobile-body-size: 0.95em;

    /* 常用间距和圆角 */
    --homepage-card-radius: 12px;
    --homepage-card-gap: 22px;
  }

  /* =========================================================
     2. Base page styles
     页面全局字体、背景、链接、分割线等基础样式。
     ========================================================= */
  body {
    color: var(--homepage-text);
    font-family: var(--homepage-font);
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

  .page__content,
  .page__content p,
  .page__content li,
  .page__content dd,
  .page__content div,
  .page__content span,
  .page__content h1,
  .page__content h2,
  .page__content h3,
  .masthead,
  .greedy-nav,
  .masthead__menu-item a,
  .greedy-nav a,
  .profile_box,
  .profile_box .author__content,
  .profile_box .author__name,
  .profile_box .author__name-zh,
  .profile_box .author__email,
  .profile_box .author__bio,
  .profile_box .author__urls li,
  .profile_box .author__urls a {
    font-family: var(--homepage-font);
  }

  .page__content {
    font-size: var(--homepage-content-size);
    line-height: 1.75;
  }

  /* 标题和顶部导航也使用与正文一致的系统字体风格。 */
  .page__content h1,
  .page__content h2,
  .page__content h3 {
    font-family: var(--homepage-font);
    font-weight: 700;
    letter-spacing: 0;
  }

  .masthead__menu-item a,
  .greedy-nav a {
    font-family: var(--homepage-font);
    font-weight: 600;
    letter-spacing: 0;
  }

  /* =========================================================
     3. Unified body text size
     同级正文统一字号：About、News、论文作者/期刊、Funding、Education、Links 等。
     ========================================================= */
  .about-text p,
  .news-list li,
  .publication-note,
  .publication-authors,
  .publication-venue,
  .content-list li,
  .service-list li,
  .info-card,
  .info-card p,
  .info-card li,
  .education-title,
  .useful-links li {
    font-size: var(--homepage-body-size);
    line-height: 1.75;
  }

  .about-text p {
    margin-bottom: 1em;
  }

  /* =========================================================
     4. Text alignment
     仅 About Me 和 News 在电脑端两端对齐；其他模块保持左对齐。
     ========================================================= */
  .page__content p,
  .page__content li,
  .page__content dd,
  .publication-card,
  .education-card,
  .content-list li,
  .service-list li,
  .info-card,
  .useful-links li {
    text-align: left;
    text-align-last: auto;
  }

  .about-text p,
  .news-list li {
    text-align: justify;
    text-align-last: left;
    text-justify: inter-word;
    hyphens: auto;
  }

  /* =========================================================
     5. News section
     News 滚动框及其滚动条样式。
     ========================================================= */
  .news-box {
    max-height: 350px;
    margin: 0;
    padding: 20px;
    overflow-y: auto;
    background: var(--homepage-bg);
    border-left: 4px solid var(--homepage-primary);
    border-radius: 0 8px 8px 0;
    scrollbar-color: var(--homepage-primary) var(--homepage-border);
    scrollbar-width: thin;
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
    margin-bottom: 12px;
  }

  .news-list li:last-child {
    margin-bottom: 0;
  }

  /* =========================================================
     6. Publication cards
     电脑端：左图右文；手机端：图片在上、文字在下。
     ========================================================= */
  .publication-list {
    margin-top: 20px;
    margin-bottom: 40px;
  }

  .publication-note {
    margin: 8px 0 18px;
  }

  .publication-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: var(--homepage-card-gap);
    box-sizing: border-box;
    width: 100%;
    margin: 20px 0;
    padding: 18px;
    background: var(--homepage-bg);
    border: 1px solid var(--homepage-border);
    border-radius: var(--homepage-card-radius);
    transition: all 0.25s ease;
  }

  .publication-card:hover {
    transform: translateY(-3px);
    border-color: var(--homepage-card-hover-border);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  }

  .publication-image {
    flex: 0 0 230px;
    order: 1;
    max-width: 230px;
  }

  .publication-image img {
    display: block;
    box-sizing: border-box;
    width: 100%;
    padding: 5px;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
  }

  .publication-content {
    flex: 1;
    order: 2;
    min-width: 0;
  }

  .publication-title {
    margin-bottom: 8px;
    font-size: 1.15em;
    font-weight: 700;
    line-height: 1.45;
  }

  .publication-title a {
    color: var(--homepage-primary);
    text-decoration: none;
  }

  .publication-title a:hover {
    color: var(--homepage-link);
    text-decoration: underline;
  }

  .publication-authors,
  .publication-venue {
    margin-bottom: 6px;
    color: #444;
  }

  .publication-venue {
    color: #555;
  }

  /* =========================================================
     7. Content lists and information cards
     Funding、Honors、Services、Courses、Students 等模块共用样式。
     ========================================================= */
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

  /* =========================================================
     8. Education cards
     电脑端和手机端均保持：左文右 logo。
     ========================================================= */
  .education-list {
    margin-top: 20px;
  }

  .education-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: var(--homepage-card-gap);
    box-sizing: border-box;
    width: 100%;
    margin: 20px 0;
    padding: 18px;
    background: var(--homepage-bg);
    border: 1px solid var(--homepage-border);
    border-radius: var(--homepage-card-radius);
    transition: all 0.25s ease;
  }

  .education-card:hover {
    transform: translateY(-3px);
    border-color: var(--homepage-card-hover-border);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  }

  .education-info {
    flex: 1 1 auto;
    order: 1;
    min-width: 0;
  }

  .education-logo {
    display: flex;
    flex: 0 0 110px;
    order: 2;
    align-items: center;
    justify-content: center;
    width: 110px;
    height: 110px;
    margin-left: auto;
    padding: 10px;
    background: #fff;
    border: 1px solid var(--homepage-border);
    border-radius: 10px;
    box-sizing: border-box;
  }

  .education-logo img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .education-title {
    color: var(--homepage-primary);
  }

  .education-title a {
    color: var(--homepage-primary);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .education-title a:hover {
    color: var(--homepage-accent);
  }

  /* =========================================================
     9. Sidebar profile
     左侧个人信息字体。注意：不要覆盖图标字体。
     ========================================================= */
  .profile_box .author__name {
    font-size: 1.35em;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  .profile_box .author__name-zh {
    font-family: var(--homepage-font);
    font-size: 1.25em;
    font-weight: 700;
    letter-spacing: 2px;
  }

  .profile_box .author__email,
  .profile_box .author__bio,
  .profile_box .author__urls li,
  .profile_box .author__urls a {
    font-size: 1em;
    line-height: 1.55;
  }

  /* 恢复图标字体，避免 DBLP / ORCID / Google Scholar 等图标变成方框。 */
  .profile_box i.fa,
  .profile_box i.fas {
    font-family: "Font Awesome 5 Free" !important;
    font-weight: 900 !important;
  }

  .profile_box i.fab {
    font-family: "Font Awesome 5 Brands" !important;
    font-weight: 400 !important;
  }

  .profile_box i.ai {
    font-family: "Academicons" !important;
    font-weight: normal !important;
  }

  /* =========================================================
     10. Responsive styles
     移动端布局与字号：论文卡片上下排列，教育卡片仍为左文右图。
     ========================================================= */
  @media screen and (max-width: 768px) {
    .page__content {
      font-size: var(--homepage-mobile-content-size);
    }

    .about-text p,
    .news-list li,
    .publication-note,
    .publication-authors,
    .publication-venue,
    .content-list li,
    .service-list li,
    .info-card,
    .info-card p,
    .info-card li,
    .education-title,
    .useful-links li {
      font-size: var(--homepage-mobile-body-size);
      line-height: 1.7;
    }

    .about-text p,
    .news-list li {
      text-align: left;
      text-align-last: auto;
      hyphens: none;
    }

    .news-box {
      max-height: 300px;
      padding: 16px;
    }

    .publication-card {
      flex-direction: column;
      align-items: stretch;
      gap: 14px;
      padding: 15px;
    }

    .publication-image {
      flex: none;
      width: 100%;
      max-width: 100%;
    }

    .publication-image img {
      aspect-ratio: 16 / 9;
    }

    .education-card {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 16px;
    }

    .education-logo {
      flex: 0 0 78px;
      width: 78px;
      height: 78px;
      margin-left: 12px;
      align-self: center;
    }

    .education-title {
      word-break: normal;
      overflow-wrap: break-word;
    }
  }

  @media screen and (max-width: 420px) {
    .education-card {
      gap: 10px;
      padding: 14px;
    }

    .education-logo {
      flex-basis: 64px;
      width: 64px;
      height: 64px;
      margin-left: 8px;
      padding: 7px;
    }
  }
</style>

<span class="anchor" id="about-me"></span>
# About Me

<div class="about-text" markdown="1">

I am currently a faculty member in the School of Computer Science and Artificial Intelligence at Zhengzhou University. I received my Ph.D. degree in Software Engineering from Zhengzhou University in June 2025, under the supervision of <a href="http://www5.zzu.edu.cn/mlis/"><strong>Prof. Yangdong Ye</strong></a>.

My research interests lie broadly in data mining and machine learning, with a particular focus on recommender systems, multimodal learning, information bottleneck, and graph representation learning. My research aims to develop effective, robust, and interpretable learning methods for recommendation and graph-based data analysis. I have published and co-authored several papers in peer-reviewed journals and conferences in related areas.

I am expected to recruit master’s students in the next admission cycle. Prospective students who are interested in recommender systems, multimodal learning, graph learning, information bottleneck, and related topics are warmly encouraged to contact me.

I also welcome academic discussions and potential collaborations with researchers working in related fields.

Official homepage is <a href="https://www7.zzu.edu.cn/csai/info/1233/3668.htm">here</a>. Feel free to contact me via <a href="mailto:qiangguo@zzu.edu.cn">Email</a> or <a href="{{ '/images/wechat.png' | relative_url }}">WeChat</a>.

</div>

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

<div class="publication-list">

  <div class="publication-card">
    <div class="publication-image">
      <img src="{{ '/images/publications/krib.png' | relative_url }}" alt="Knowledge-refined information bottleneck for contrastive recommendation" loading="lazy">
    </div>
    <div class="publication-content">
      <div class="publication-title">
        <a href="https://www.sciencedirect.com/science/article/pii/S0957417425022912" target="_blank" rel="noopener">
          Knowledge-refined information bottleneck for contrastive recommendation
        </a>
      </div>
      <div class="publication-authors">
        <strong>Qiang Guo</strong>, Bin Wu, Zhongchuan Sun, Haichuan Fang, Yangdong Ye*
      </div>
      <div class="publication-venue">
        Expert Systems with Applications, 2025. (中科院 1 区 SCI, IF: 7.5)
      </div>
    </div>
  </div>

  <div class="publication-card">
    <div class="publication-image">
      <img src="{{ '/images/publications/dcib.png' | relative_url }}" alt="DCIB: Dual contrastive information bottleneck for knowledge-aware recommendation" loading="lazy">
    </div>
    <div class="publication-content">
      <div class="publication-title">
        <a href="https://www.sciencedirect.com/science/article/abs/pii/S030645732400339X" target="_blank" rel="noopener">
          DCIB: Dual contrastive information bottleneck for knowledge-aware recommendation
        </a>
      </div>
      <div class="publication-authors">
        <strong>Qiang Guo</strong>, Jialong Hai, Zhongchuan Sun, Bin Wu, Yangdong Ye*
      </div>
      <div class="publication-venue">
        Information Processing &amp; Management, 2025. (中科院 1 区 SCI, IF: 7.4)
      </div>
    </div>
  </div>

  <div class="publication-card">
    <div class="publication-image">
      <img src="{{ '/images/publications/dcib.png' | relative_url }}" alt="Multimodal nonredundant clustering via sufficiency complementary mining" loading="lazy">
    </div>
    <div class="publication-content">
      <div class="publication-title">
        <a href="https://ieeexplore.ieee.org/abstract/document/10770014" target="_blank" rel="noopener">
          Multimodal nonredundant clustering via sufficiency complementary mining
        </a>
      </div>
      <div class="publication-authors">
        Yiqiao Mao, Xiaoqiang Yan, <strong>Qiang Guo*</strong>, Yangdong Ye*
      </div>
      <div class="publication-venue">
        IEEE Transactions on Industrial Informatics, 2025. (中科院1区 SCI, IF: 11.7)
      </div>
    </div>
  </div>

  <div class="publication-card">
    <div class="publication-image">
      <img src="{{ '/images/publications/rgbt-crowd.png' | relative_url }}" alt="Consistency-constrained RGB-T crowd counting via mutual information maximization" loading="lazy">
    </div>
    <div class="publication-content">
      <div class="publication-title">
        <a href="https://link.springer.com/article/10.1007/s40747-024-01427-x" target="_blank" rel="noopener">
          Consistency-constrained RGB-T crowd counting via mutual information maximization
        </a>
      </div>
      <div class="publication-authors">
        <strong>Qiang Guo</strong>, Pengcheng Yuan, Xiangming Huang, Yangdong Ye*
      </div>
      <div class="publication-venue">
        Complex &amp; Intelligent Systems, 2024. (中科院 2 区 SCI, IF: 5.0)
      </div>
    </div>
  </div>

  <div class="publication-card">
    <div class="publication-image">
      <img src="{{ '/images/publications/cross-hierarchy.png' | relative_url }}" alt="Learning a deep network with cross-hierarchy aggregation for crowd counting" loading="lazy">
    </div>
    <div class="publication-content">
      <div class="publication-title">
        <a href="https://www.sciencedirect.com/science/article/abs/pii/S0950705120308200" target="_blank" rel="noopener">
          Learning a deep network with cross-hierarchy aggregation for crowd counting
        </a>
      </div>
      <div class="publication-authors">
        <strong>Qiang Guo</strong>, Xin Zeng, Shizhe Hu, Sonephet Phoummixay, Yangdong Ye*
      </div>
      <div class="publication-venue">
        Knowledge-Based Systems, 2021. (中科院 1 区 SCI, IF: 8.1)
      </div>
    </div>
  </div>

</div>

<hr>

<span class="anchor" id="funding"></span>
# 💰 Funding

<ul class="content-list">
  <li>To be updated.</li>
</ul>

<hr>
<!--
<span class="anchor" id="honors"></span>
# 🎖 Honors

<ul class="content-list">
  <li>To be updated.</li>
</ul>

<hr>

<span class="anchor" id="services"></span>
# 🤝 Services

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

<span class="anchor" id="courses"></span>
# 👨‍🏫 Courses

<div class="info-card">
  <p>Teaching information will be updated as courses are finalized.</p>
  <ul>
    <li><strong>Course Name</strong>, Undergraduate/Graduate, Zhengzhou University, Semester.</li>
  </ul>
</div>

<hr>

<span class="anchor" id="students"></span>
# 🎓 Students

<div class="info-card">
  <p>I am expected to recruit master’s students in the next admission cycle. Students interested in recommender systems, multimodal learning, graph representation learning, information bottleneck, and related machine learning topics are welcome to contact me.</p>
  <p>Please include your CV, transcript, research interests, and any representative projects or publications when contacting me.</p>
</div>

<hr>
-->

<span class="anchor" id="education"></span>
# 📖 Education

<div class="education-list">

  <div class="education-card">
    <div class="education-info">
      <div class="education-title">
        <strong>2021.09 - 2025.06:</strong><br>
        Zhengzhou University, Ph.D. in Software Engineering<br>
        Supervised by <a href="http://www5.zzu.edu.cn/mlis/" target="_blank" rel="noopener"><strong>Prof. Yangdong Ye</strong></a>
      </div>
    </div>

    <div class="education-logo">
      <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University" loading="lazy">
    </div>
  </div>

  <div class="education-card">
    <div class="education-info">
      <div class="education-title">
        <strong>2018.09 - 2021.06:</strong><br>
        Zhengzhou University, M.Sc. in Computer Science and Technology<br>
        Supervised by <a href="http://www5.zzu.edu.cn/mlis/" target="_blank" rel="noopener"><strong>Prof. Yangdong Ye</strong></a>
      </div>
    </div>

    <div class="education-logo">
      <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University" loading="lazy">
    </div>
  </div>

  <div class="education-card">
    <div class="education-info">
      <div class="education-title">
        <strong>2010.09 - 2014.06:</strong><br>
        Shenzhen University, B.Sc. in Software Engineering
      </div>
    </div>

    <div class="education-logo">
      <img src="{{ '/images/szulogo.png' | relative_url }}" alt="Shenzhen University" loading="lazy">
    </div>
  </div>

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
