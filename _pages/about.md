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

/* ===============================
   Global font and text style
   English: clean sans-serif
   Chinese: SimSun
   =============================== */

.page__content,
.page__content p,
.page__content li,
.page__content dd,
.page__content div,
.page__content span {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "SimSun", "宋体", sans-serif;
}

/* 页面主要正文大小：恢复到之前较大的效果 */
.page__content > p,
.about-text p,
.news-list li,
.publication-authors,
.publication-venue,
.education-title,
.funding-list li,
.honors-list li,
.service-list li,
.course-list li,
.students-list li,
.useful-links li {
  font-size: 1.2em;
  line-height: 1.65;
}

/* 中文内容优先使用宋体 */
:lang(zh),
.zh,
.chinese {
  font-family: "SimSun", "宋体", serif;
}

/* 默认：除 About Me 和 News 外，其余内容保持左对齐 */
.page__content p,
.page__content li,
.page__content dd,
.publication-card,
.education-card,
.funding-list li,
.honors-list li,
.service-list li,
.course-list li,
.students-list li,
.useful-links li {
  text-align: left;
  text-align-last: auto;
}

/* 仅 About Me 和 News 两端对齐 */
.about-text p,
.news-list li {
  text-align: justify;
  text-align-last: left;
  text-justify: inter-word;
  hyphens: auto;
}

/* 手机端：两端对齐容易拉开词距，恢复自然左对齐 */
@media screen and (max-width: 600px) {
  .about-text p,
  .news-list li {
    text-align: left;
    text-align-last: auto;
    hyphens: none;
  }
}


/* ===============================
   News box
   =============================== */

.news-box {
  max-height: 350px;
  overflow-y: auto;
  padding: 20px;
  background: #f8f9fa;
  border-left: 4px solid #2c3e50;
  margin: 0;
  border-radius: 0 8px 8px 0;
}

.news-list {
  list-style-type: none;
  padding-left: 0;
  margin: 0;
}

.news-list li {
  margin-bottom: 12px;
  line-height: 1.65;
}

.news-list li:last-child {
  margin-bottom: 0;
}

.news-box::-webkit-scrollbar {
  width: 8px;
}

.news-box::-webkit-scrollbar-track {
  background: #e9ecef;
  border-radius: 4px;
}

.news-box::-webkit-scrollbar-thumb {
  background: #2c3e50;
  border-radius: 4px;
}

.news-box::-webkit-scrollbar-thumb:hover {
  background: #1a252f;
}


/* ===============================
   Publication cards
   Left image + right paper information
   =============================== */

.publication-list {
  margin-top: 20px;
}

.publication-card {
  display: flex;
  align-items: center;
  gap: 22px;
  width: 100%;
  box-sizing: border-box;
  margin: 20px 0;
  padding: 18px;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  transition: all 0.25s ease;
}

.publication-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.10);
  border-color: #dee2e6;
}

.publication-image {
  flex: 0 0 230px;
  max-width: 230px;
}

.publication-image img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
  border-radius: 10px;
  border: 1px solid #ddd;
  background: #fff;
  padding: 5px;
  box-sizing: border-box;
}

.publication-content {
  flex: 1;
  min-width: 0;
}

.publication-title {
  margin-bottom: 8px;
  font-size: 1.15em;
  line-height: 1.45;
  font-weight: 700;
}

.publication-title a {
  color: #2c3e50;
  text-decoration: none;
}

.publication-title a:hover {
  color: #0066cc;
  text-decoration: underline;
}

.publication-authors,
.publication-venue {
  margin-bottom: 6px;
  line-height: 1.55;
  color: #444;
}

.publication-venue {
  color: #555;
}

.publication-note {
  margin: 8px 0 18px;
  line-height: 1.6;
}


/* ===============================
   Education cards
   Left logo + right education information
   =============================== */

.education-list {
  margin-top: 20px;
}

.education-card {
  display: flex;
  align-items: center;
  gap: 22px;
  width: 100%;
  box-sizing: border-box;
  margin: 20px 0;
  padding: 18px;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  transition: all 0.25s ease;
}

.education-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.10);
  border-color: #dee2e6;
}

.education-logo {
  flex: 0 0 110px;
  width: 110px;
  height: 110px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 10px;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #e9ecef;
}

.education-logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.education-info {
  flex: 1;
  min-width: 0;
}

.education-title {
  font-size: 1.15em;
  line-height: 1.55;
  color: #2c3e50;
}


/* ===============================
   Responsive layout for mobile devices
   =============================== */

@media screen and (max-width: 768px) {
  .news-box {
    max-height: 300px;
    padding: 16px;
  }

  .publication-card,
  .education-card {
    flex-direction: column;
    align-items: stretch;
    gap: 14px;
    padding: 15px;
  }

  .publication-image {
    flex: none;
    max-width: 100%;
    width: 100%;
  }

  .publication-image img {
    aspect-ratio: 16 / 9;
  }

  .education-logo {
    width: 90px;
    height: 90px;
    flex: none;
    align-self: center;
  }

  .publication-title,
  .education-title {
    font-size: 1.05em;
  }

  .publication-authors,
  .publication-venue,
  .news-list li {
    font-size: 1em;
    line-height: 1.6;
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

<span class="anchor" id="publications"></span>
# 📝 Selected Publications ([Full List](https://scholar.google.com/citations?user=CpUZV-cAAAAJ&hl=en))

<p class="publication-note"><strong>#</strong> indicates equal contribution, and <strong>*</strong> indicates the corresponding author.</p>

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
    <div class="education-logo">
      <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University" loading="lazy">
    </div>
    <div class="education-info">
      <div class="education-title">
        <strong>2021.09 - 2025.06:</strong><br>
        Zhengzhou University, Ph.D. in Software Engineering<br>
        Supervised by <a href="http://www5.zzu.edu.cn/mlis/" target="_blank" rel="noopener"><strong>Prof. Yangdong Ye</strong></a>
      </div>
    </div>
  </div>

  <div class="education-card">
    <div class="education-logo">
      <img src="{{ '/images/zzulogo.png' | relative_url }}" alt="Zhengzhou University" loading="lazy">
    </div>
    <div class="education-info">
      <div class="education-title">
        <strong>2018.09 - 2021.06:</strong><br>
        Zhengzhou University, M.Sc. in Computer Science and Technology<br>
        Supervised by <a href="http://www5.zzu.edu.cn/mlis/" target="_blank" rel="noopener"><strong>Prof. Yangdong Ye</strong></a>
      </div>
    </div>
  </div>

  <div class="education-card">
    <div class="education-logo">
      <img src="{{ '/images/szulogo.png' | relative_url }}" alt="Shenzhen University" loading="lazy">
    </div>
    <div class="education-info">
      <div class="education-title">
        <strong>2010.09 - 2014.06:</strong><br>
        Shenzhen University, B.Sc. in Software Engineering
      </div>
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
