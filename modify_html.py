import os
import re

html_path = '/Users/sahidafridi/portfolio/index.html'
with open(html_path, 'r') as f:
    content = f.read()

snippets = {
    'JavaScript (ES6+)': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 25s;">
                            <pre><code><span class="keyword">class</span> <span class="function">VirtualDOM</span> {
  <span class="function">constructor</span>() {
    <span class="keyword">this</span>.<span class="variable">nodes</span> = <span class="keyword">new</span> <span class="function">Map</span>();
    <span class="keyword">this</span>.<span class="variable">isRendering</span> = <span class="boolean">false</span>;
  }

  <span class="keyword">async</span> <span class="function">update</span>(<span class="variable">component</span>, <span class="variable">state</span>) {
    <span class="keyword">const</span> <span class="variable">oldNode</span> = <span class="keyword">this</span>.<span class="variable">nodes</span>.<span class="function">get</span>(<span class="variable">component</span>.<span class="variable">id</span>);
    <span class="keyword">const</span> <span class="variable">newNode</span> = <span class="keyword">await</span> <span class="variable">component</span>.<span class="function">render</span>(<span class="variable">state</span>);
    
    <span class="keyword">const</span> <span class="variable">patches</span> = <span class="keyword">this</span>.<span class="function">diff</span>(<span class="variable">oldNode</span>, <span class="variable">newNode</span>);
    <span class="function">requestAnimationFrame</span>(() =&gt; {
      <span class="keyword">this</span>.<span class="function">apply</span>(<span class="variable">component</span>.<span class="variable">element</span>, <span class="variable">patches</span>);
      <span class="keyword">this</span>.<span class="variable">nodes</span>.<span class="function">set</span>(<span class="variable">component</span>.<span class="variable">id</span>, <span class="variable">newNode</span>);
    });
  }
}</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">class</span> <span class="function">VirtualDOM</span> {
  <span class="function">constructor</span>() {
    <span class="keyword">this</span>.<span class="variable">nodes</span> = <span class="keyword">new</span> <span class="function">Map</span>();
    <span class="keyword">this</span>.<span class="variable">isRendering</span> = <span class="boolean">false</span>;
  }

  <span class="keyword">async</span> <span class="function">update</span>(<span class="variable">component</span>, <span class="variable">state</span>) {
    <span class="keyword">const</span> <span class="variable">oldNode</span> = <span class="keyword">this</span>.<span class="variable">nodes</span>.<span class="function">get</span>(<span class="variable">component</span>.<span class="variable">id</span>);
    <span class="keyword">const</span> <span class="variable">newNode</span> = <span class="keyword">await</span> <span class="variable">component</span>.<span class="function">render</span>(<span class="variable">state</span>);
    
    <span class="keyword">const</span> <span class="variable">patches</span> = <span class="keyword">this</span>.<span class="function">diff</span>(<span class="variable">oldNode</span>, <span class="variable">newNode</span>);
    <span class="function">requestAnimationFrame</span>(() =&gt; {
      <span class="keyword">this</span>.<span class="function">apply</span>(<span class="variable">component</span>.<span class="variable">element</span>, <span class="variable">patches</span>);
      <span class="keyword">this</span>.<span class="variable">nodes</span>.<span class="function">set</span>(<span class="variable">component</span>.<span class="variable">id</span>, <span class="variable">newNode</span>);
    });
  }
}</code></pre>
                        </div>
                    </div>''',
    
    'CSS3': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 20s;">
                            <pre><code><span class="keyword">@keyframes</span> <span class="function">neonGlow</span> {
  <span class="keyword">0%</span> {
    <span class="variable">box-shadow</span>: 0 0 5px <span class="string">#fff</span>,
                0 0 10px <span class="string">#fff</span>,
                0 0 20px <span class="string">#0fa</span>,
                0 0 40px <span class="string">#0fa</span>;
  }
  <span class="keyword">100%</span> {
    <span class="variable">box-shadow</span>: 0 0 2px <span class="string">#fff</span>,
                0 0 5px <span class="string">#fff</span>,
                0 0 10px <span class="string">#0fa</span>,
                0 0 20px <span class="string">#0fa</span>;
  }
}

<span class="keyword">.glass-card</span> {
  <span class="variable">background</span>: <span class="function">rgba</span>(<span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">0.05</span>);
  <span class="variable">backdrop-filter</span>: <span class="function">blur</span>(10px);
  <span class="variable">border</span>: 1px solid <span class="function">rgba</span>(<span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">0.1</span>);
  <span class="variable">transition</span>: transform 0.3s ease;
}</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">@keyframes</span> <span class="function">neonGlow</span> {
  <span class="keyword">0%</span> {
    <span class="variable">box-shadow</span>: 0 0 5px <span class="string">#fff</span>,
                0 0 10px <span class="string">#fff</span>,
                0 0 20px <span class="string">#0fa</span>,
                0 0 40px <span class="string">#0fa</span>;
  }
  <span class="keyword">100%</span> {
    <span class="variable">box-shadow</span>: 0 0 2px <span class="string">#fff</span>,
                0 0 5px <span class="string">#fff</span>,
                0 0 10px <span class="string">#0fa</span>,
                0 0 20px <span class="string">#0fa</span>;
  }
}

<span class="keyword">.glass-card</span> {
  <span class="variable">background</span>: <span class="function">rgba</span>(<span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">0.05</span>);
  <span class="variable">backdrop-filter</span>: <span class="function">blur</span>(10px);
  <span class="variable">border</span>: 1px solid <span class="function">rgba</span>(<span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">255</span>, <span class="boolean">0.1</span>);
  <span class="variable">transition</span>: transform 0.3s ease;
}</code></pre>
                        </div>
                    </div>''',
                    
    'React Native': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 25s;">
                            <pre><code><span class="keyword">import</span> { <span class="variable">View</span>, <span class="variable">Text</span>, <span class="variable">StyleSheet</span>, <span class="variable">Animated</span> } <span class="keyword">from</span> <span class="string">'react-native'</span>;
<span class="keyword">import</span> { <span class="variable">useRef</span>, <span class="variable">useEffect</span> } <span class="keyword">from</span> <span class="string">'react'</span>;

<span class="keyword">export default function</span> <span class="function">SwipeCard</span>() {
  <span class="keyword">const</span> <span class="variable">pan</span> = <span class="function">useRef</span>(<span class="keyword">new</span> <span class="variable">Animated</span>.<span class="function">ValueXY</span>()).<span class="variable">current</span>;
  
  <span class="function">useEffect</span>(() =&gt; {
    <span class="variable">Animated</span>.<span class="function">spring</span>(<span class="variable">pan</span>, {
      <span class="variable">toValue</span>: { <span class="variable">x</span>: <span class="boolean">0</span>, <span class="variable">y</span>: <span class="boolean">0</span> },
      <span class="variable">useNativeDriver</span>: <span class="boolean">true</span>,
    }).<span class="function">start</span>();
  }, []);

  <span class="keyword">return</span> (
    <span class="tag">&lt;Animated.View</span>
      <span class="variable">style</span>={{
        <span class="variable">transform</span>: [{ <span class="variable">translateX</span>: <span class="variable">pan</span>.<span class="variable">x</span> }, { <span class="variable">translateY</span>: <span class="variable">pan</span>.<span class="variable">y</span> }]
      }}
    <span class="tag">&gt;</span>
      <span class="tag">&lt;Text</span> <span class="variable">style</span>={<span class="variable">styles</span>.<span class="variable">title</span>}<span class="tag">&gt;</span>Swipe Me<span class="tag">&lt;/Text&gt;</span>
    <span class="tag">&lt;/Animated.View&gt;</span>
  );
}</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">import</span> { <span class="variable">View</span>, <span class="variable">Text</span>, <span class="variable">StyleSheet</span>, <span class="variable">Animated</span> } <span class="keyword">from</span> <span class="string">'react-native'</span>;
<span class="keyword">import</span> { <span class="variable">useRef</span>, <span class="variable">useEffect</span> } <span class="keyword">from</span> <span class="string">'react'</span>;

<span class="keyword">export default function</span> <span class="function">SwipeCard</span>() {
  <span class="keyword">const</span> <span class="variable">pan</span> = <span class="function">useRef</span>(<span class="keyword">new</span> <span class="variable">Animated</span>.<span class="function">ValueXY</span>()).<span class="variable">current</span>;
  
  <span class="function">useEffect</span>(() =&gt; {
    <span class="variable">Animated</span>.<span class="function">spring</span>(<span class="variable">pan</span>, {
      <span class="variable">toValue</span>: { <span class="variable">x</span>: <span class="boolean">0</span>, <span class="variable">y</span>: <span class="boolean">0</span> },
      <span class="variable">useNativeDriver</span>: <span class="boolean">true</span>,
    }).<span class="function">start</span>();
  }, []);

  <span class="keyword">return</span> (
    <span class="tag">&lt;Animated.View</span>
      <span class="variable">style</span>={{
        <span class="variable">transform</span>: [{ <span class="variable">translateX</span>: <span class="variable">pan</span>.<span class="variable">x</span> }, { <span class="variable">translateY</span>: <span class="variable">pan</span>.<span class="variable">y</span> }]
      }}
    <span class="tag">&gt;</span>
      <span class="tag">&lt;Text</span> <span class="variable">style</span>={<span class="variable">styles</span>.<span class="variable">title</span>}<span class="tag">&gt;</span>Swipe Me<span class="tag">&lt;/Text&gt;</span>
    <span class="tag">&lt;/Animated.View&gt;</span>
  );
}</code></pre>
                        </div>
                    </div>''',
                    
    'Supabase': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 25s;">
                            <pre><code><span class="keyword">import</span> { <span class="variable">createClient</span> } <span class="keyword">from</span> <span class="string">'@supabase/supabase-js'</span>;

<span class="keyword">const</span> <span class="variable">supabaseUrl</span> = <span class="string">'https://xyzcompany.supabase.co'</span>;
<span class="keyword">const</span> <span class="variable">supabaseKey</span> = <span class="variable">process</span>.<span class="variable">env</span>.<span class="variable">SUPABASE_KEY</span>;
<span class="keyword">const</span> <span class="variable">supabase</span> = <span class="function">createClient</span>(<span class="variable">supabaseUrl</span>, <span class="variable">supabaseKey</span>);

<span class="keyword">async function</span> <span class="function">getRealtimeUpdates</span>() {
  <span class="keyword">const</span> <span class="variable">channel</span> = <span class="variable">supabase</span>
    .<span class="function">channel</span>(<span class="string">'schema-db-changes'</span>)
    .<span class="function">on</span>(
      <span class="string">'postgres_changes'</span>,
      { <span class="variable">event</span>: <span class="string">'*'</span>, <span class="variable">schema</span>: <span class="string">'public'</span>, <span class="variable">table</span>: <span class="string">'messages'</span> },
      (<span class="variable">payload</span>) =&gt; <span class="variable">console</span>.<span class="function">log</span>(<span class="variable">payload</span>)
    )
    .<span class="function">subscribe</span>();
    
  <span class="keyword">return</span> <span class="variable">channel</span>;
}

<span class="keyword">const</span> { <span class="variable">data</span>, <span class="variable">error</span> } = <span class="keyword">await</span> <span class="variable">supabase</span>
  .<span class="function">from</span>(<span class="string">'users'</span>)
  .<span class="function">select</span>(<span class="string">'id, name, avatar_url'</span>)
  .<span class="function">eq</span>(<span class="string">'status'</span>, <span class="string">'ONLINE'</span>);</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">import</span> { <span class="variable">createClient</span> } <span class="keyword">from</span> <span class="string">'@supabase/supabase-js'</span>;

<span class="keyword">const</span> <span class="variable">supabaseUrl</span> = <span class="string">'https://xyzcompany.supabase.co'</span>;
<span class="keyword">const</span> <span class="variable">supabaseKey</span> = <span class="variable">process</span>.<span class="variable">env</span>.<span class="variable">SUPABASE_KEY</span>;
<span class="keyword">const</span> <span class="variable">supabase</span> = <span class="function">createClient</span>(<span class="variable">supabaseUrl</span>, <span class="variable">supabaseKey</span>);

<span class="keyword">async function</span> <span class="function">getRealtimeUpdates</span>() {
  <span class="keyword">const</span> <span class="variable">channel</span> = <span class="variable">supabase</span>
    .<span class="function">channel</span>(<span class="string">'schema-db-changes'</span>)
    .<span class="function">on</span>(
      <span class="string">'postgres_changes'</span>,
      { <span class="variable">event</span>: <span class="string">'*'</span>, <span class="variable">schema</span>: <span class="string">'public'</span>, <span class="variable">table</span>: <span class="string">'messages'</span> },
      (<span class="variable">payload</span>) =&gt; <span class="variable">console</span>.<span class="function">log</span>(<span class="variable">payload</span>)
    )
    .<span class="function">subscribe</span>();
    
  <span class="keyword">return</span> <span class="variable">channel</span>;
}

<span class="keyword">const</span> { <span class="variable">data</span>, <span class="variable">error</span> } = <span class="keyword">await</span> <span class="variable">supabase</span>
  .<span class="function">from</span>(<span class="string">'users'</span>)
  .<span class="function">select</span>(<span class="string">'id, name, avatar_url'</span>)
  .<span class="function">eq</span>(<span class="string">'status'</span>, <span class="string">'ONLINE'</span>);</code></pre>
                        </div>
                    </div>''',
                    
    'HTML5': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 18s;">
                            <pre><code><span class="tag">&lt;!DOCTYPE html&gt;</span>
<span class="tag">&lt;html</span> <span class="variable">lang</span>=<span class="string">"en"</span><span class="tag">&gt;</span>
<span class="tag">&lt;head&gt;</span>
  <span class="tag">&lt;meta</span> <span class="variable">charset</span>=<span class="string">"UTF-8"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;meta</span> <span class="variable">name</span>=<span class="string">"viewport"</span> <span class="variable">content</span>=<span class="string">"width=device-width"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;title&gt;</span>Semantic HTML5<span class="tag">&lt;/title&gt;</span>
<span class="tag">&lt;/head&gt;</span>
<span class="tag">&lt;body&gt;</span>
  <span class="tag">&lt;header&gt;</span>
    <span class="tag">&lt;nav</span> <span class="variable">aria-label</span>=<span class="string">"Primary"</span><span class="tag">&gt;</span>
      <span class="tag">&lt;ul&gt;</span>
        <span class="tag">&lt;li&gt;&lt;a</span> <span class="variable">href</span>=<span class="string">"#home"</span><span class="tag">&gt;</span>Home<span class="tag">&lt;/a&gt;&lt;/li&gt;</span>
        <span class="tag">&lt;li&gt;&lt;a</span> <span class="variable">href</span>=<span class="string">"#about"</span><span class="tag">&gt;</span>About<span class="tag">&lt;/a&gt;&lt;/li&gt;</span>
      <span class="tag">&lt;/ul&gt;</span>
    <span class="tag">&lt;/nav&gt;</span>
  <span class="tag">&lt;/header&gt;</span>
  <span class="tag">&lt;main&gt;</span>
    <span class="tag">&lt;article&gt;</span>
      <span class="tag">&lt;h1&gt;</span>Semantic Web<span class="tag">&lt;/h1&gt;</span>
      <span class="tag">&lt;p&gt;</span>Accessibility first.<span class="tag">&lt;/p&gt;</span>
    <span class="tag">&lt;/article&gt;</span>
  <span class="tag">&lt;/main&gt;</span>
<span class="tag">&lt;/body&gt;</span>
<span class="tag">&lt;/html&gt;</span></code></pre>
                            <pre aria-hidden="true"><code><span class="tag">&lt;!DOCTYPE html&gt;</span>
<span class="tag">&lt;html</span> <span class="variable">lang</span>=<span class="string">"en"</span><span class="tag">&gt;</span>
<span class="tag">&lt;head&gt;</span>
  <span class="tag">&lt;meta</span> <span class="variable">charset</span>=<span class="string">"UTF-8"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;meta</span> <span class="variable">name</span>=<span class="string">"viewport"</span> <span class="variable">content</span>=<span class="string">"width=device-width"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;title&gt;</span>Semantic HTML5<span class="tag">&lt;/title&gt;</span>
<span class="tag">&lt;/head&gt;</span>
<span class="tag">&lt;body&gt;</span>
  <span class="tag">&lt;header&gt;</span>
    <span class="tag">&lt;nav</span> <span class="variable">aria-label</span>=<span class="string">"Primary"</span><span class="tag">&gt;</span>
      <span class="tag">&lt;ul&gt;</span>
        <span class="tag">&lt;li&gt;&lt;a</span> <span class="variable">href</span>=<span class="string">"#home"</span><span class="tag">&gt;</span>Home<span class="tag">&lt;/a&gt;&lt;/li&gt;</span>
        <span class="tag">&lt;li&gt;&lt;a</span> <span class="variable">href</span>=<span class="string">"#about"</span><span class="tag">&gt;</span>About<span class="tag">&lt;/a&gt;&lt;/li&gt;</span>
      <span class="tag">&lt;/ul&gt;</span>
    <span class="tag">&lt;/nav&gt;</span>
  <span class="tag">&lt;/header&gt;</span>
  <span class="tag">&lt;main&gt;</span>
    <span class="tag">&lt;article&gt;</span>
      <span class="tag">&lt;h1&gt;</span>Semantic Web<span class="tag">&lt;/h1&gt;</span>
      <span class="tag">&lt;p&gt;</span>Accessibility first.<span class="tag">&lt;/p&gt;</span>
    <span class="tag">&lt;/article&gt;</span>
  <span class="tag">&lt;/main&gt;</span>
<span class="tag">&lt;/body&gt;</span>
<span class="tag">&lt;/html&gt;</span></code></pre>
                        </div>
                    </div>''',
                    
    'Git': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 20s;">
                            <pre><code><span class="keyword">$</span> <span class="function">git</span> <span class="variable">commit</span> -m <span class="string">"Fix async bugs"</span>
[main 7f3a1b2] Fix async bugs
 3 files changed, 45 insertions(+), 12 deletions(-)

<span class="keyword">$</span> <span class="function">git</span> <span class="variable">push</span> origin main
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 10 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 842 bytes
Total 6 (delta 4), reused 0 (delta 0)
To github.com:sahidafridi/portfolio.git
   d8f3e2a..7f3a1b2  main -&gt; main

<span class="keyword">$</span> <span class="function">git</span> <span class="variable">status</span>
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">$</span> <span class="function">git</span> <span class="variable">commit</span> -m <span class="string">"Fix async bugs"</span>
[main 7f3a1b2] Fix async bugs
 3 files changed, 45 insertions(+), 12 deletions(-)

<span class="keyword">$</span> <span class="function">git</span> <span class="variable">push</span> origin main
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 10 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 842 bytes
Total 6 (delta 4), reused 0 (delta 0)
To github.com:sahidafridi/portfolio.git
   d8f3e2a..7f3a1b2  main -&gt; main

<span class="keyword">$</span> <span class="function">git</span> <span class="variable">status</span>
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean</code></pre>
                        </div>
                    </div>''',
                    
    'GitHub': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 20s;">
                            <pre><code><span class="keyword">name</span>: <span class="variable">CI/CD Pipeline</span>

<span class="keyword">on</span>:
  <span class="keyword">push</span>:
    <span class="variable">branches</span>: [ <span class="string">"main"</span> ]

<span class="keyword">jobs</span>:
  <span class="function">build</span>:
    <span class="variable">runs-on</span>: ubuntu-latest
    <span class="keyword">steps</span>:
    - <span class="variable">uses</span>: actions/checkout@v3
    - <span class="keyword">name</span>: <span class="variable">Use Node.js</span>
      <span class="variable">uses</span>: actions/setup-node@v3
      <span class="keyword">with</span>:
        <span class="variable">node-version</span>: <span class="string">'18.x'</span>
    - <span class="keyword">run</span>: <span class="variable">npm ci</span>
    - <span class="keyword">run</span>: <span class="variable">npm run build</span>
    - <span class="keyword">run</span>: <span class="variable">npm test</span></code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">name</span>: <span class="variable">CI/CD Pipeline</span>

<span class="keyword">on</span>:
  <span class="keyword">push</span>:
    <span class="variable">branches</span>: [ <span class="string">"main"</span> ]

<span class="keyword">jobs</span>:
  <span class="function">build</span>:
    <span class="variable">runs-on</span>: ubuntu-latest
    <span class="keyword">steps</span>:
    - <span class="variable">uses</span>: actions/checkout@v3
    - <span class="keyword">name</span>: <span class="variable">Use Node.js</span>
      <span class="variable">uses</span>: actions/setup-node@v3
      <span class="keyword">with</span>:
        <span class="variable">node-version</span>: <span class="string">'18.x'</span>
    - <span class="keyword">run</span>: <span class="variable">npm ci</span>
    - <span class="keyword">run</span>: <span class="variable">npm run build</span>
    - <span class="keyword">run</span>: <span class="variable">npm test</span></code></pre>
                        </div>
                    </div>''',
                    
    'FormSubmit': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 22s;">
                            <pre><code><span class="tag">&lt;form</span> <span class="variable">action</span>=<span class="string">"https://formsubmit.co/your@email.com"</span> <span class="variable">method</span>=<span class="string">"POST"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_subject"</span> <span class="variable">value</span>=<span class="string">"New Message!"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_next"</span> <span class="variable">value</span>=<span class="string">"https://yourdomain.co/thanks"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_captcha"</span> <span class="variable">value</span>=<span class="string">"false"</span><span class="tag">&gt;</span>
  
  <span class="tag">&lt;div</span> <span class="variable">class</span>=<span class="string">"form-group"</span><span class="tag">&gt;</span>
    <span class="tag">&lt;label&gt;</span>Email Address<span class="tag">&lt;/label&gt;</span>
    <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"email"</span> <span class="variable">name</span>=<span class="string">"email"</span> <span class="variable">required</span><span class="tag">&gt;</span>
  <span class="tag">&lt;/div&gt;</span>
  
  <span class="tag">&lt;div</span> <span class="variable">class</span>=<span class="string">"form-group"</span><span class="tag">&gt;</span>
    <span class="tag">&lt;label&gt;</span>Message<span class="tag">&lt;/label&gt;</span>
    <span class="tag">&lt;textarea</span> <span class="variable">name</span>=<span class="string">"message"</span> <span class="variable">required</span><span class="tag">&gt;&lt;/textarea&gt;</span>
  <span class="tag">&lt;/div&gt;</span>
  
  <span class="tag">&lt;button</span> <span class="variable">type</span>=<span class="string">"submit"</span><span class="tag">&gt;</span>Send<span class="tag">&lt;/button&gt;</span>
<span class="tag">&lt;/form&gt;</span></code></pre>
                            <pre aria-hidden="true"><code><span class="tag">&lt;form</span> <span class="variable">action</span>=<span class="string">"https://formsubmit.co/your@email.com"</span> <span class="variable">method</span>=<span class="string">"POST"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_subject"</span> <span class="variable">value</span>=<span class="string">"New Message!"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_next"</span> <span class="variable">value</span>=<span class="string">"https://yourdomain.co/thanks"</span><span class="tag">&gt;</span>
  <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"hidden"</span> <span class="variable">name</span>=<span class="string">"_captcha"</span> <span class="variable">value</span>=<span class="string">"false"</span><span class="tag">&gt;</span>
  
  <span class="tag">&lt;div</span> <span class="variable">class</span>=<span class="string">"form-group"</span><span class="tag">&gt;</span>
    <span class="tag">&lt;label&gt;</span>Email Address<span class="tag">&lt;/label&gt;</span>
    <span class="tag">&lt;input</span> <span class="variable">type</span>=<span class="string">"email"</span> <span class="variable">name</span>=<span class="string">"email"</span> <span class="variable">required</span><span class="tag">&gt;</span>
  <span class="tag">&lt;/div&gt;</span>
  
  <span class="tag">&lt;div</span> <span class="variable">class</span>=<span class="string">"form-group"</span><span class="tag">&gt;</span>
    <span class="tag">&lt;label&gt;</span>Message<span class="tag">&lt;/label&gt;</span>
    <span class="tag">&lt;textarea</span> <span class="variable">name</span>=<span class="string">"message"</span> <span class="variable">required</span><span class="tag">&gt;&lt;/textarea&gt;</span>
  <span class="tag">&lt;/div&gt;</span>
  
  <span class="tag">&lt;button</span> <span class="variable">type</span>=<span class="string">"submit"</span><span class="tag">&gt;</span>Send<span class="tag">&lt;/button&gt;</span>
<span class="tag">&lt;/form&gt;</span></code></pre>
                        </div>
                    </div>''',
                    
    'Hostinger': '''                    <div class="code-snippet-bg">
                        <div class="code-scroll-container" style="animation-duration: 20s;">
                            <pre><code><span class="keyword">$</span> <span class="function">ssh</span> <span class="variable">user@hostinger-vps.com</span>
Welcome to Ubuntu 22.04 LTS

<span class="keyword">user@vps:~$</span> <span class="function">systemctl</span> <span class="variable">status</span> nginx
● nginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running)
     Docs: man:nginx(8)

<span class="keyword">user@vps:~$</span> <span class="function">cat</span> <span class="string">/etc/nginx/sites-available/portfolio</span>
server {
    listen 80;
    server_name sahidafridi.com;
    
    location / {
        root /var/www/portfolio/html;
        index index.html;
        try_files $uri $uri/ =404;
    }
}</code></pre>
                            <pre aria-hidden="true"><code><span class="keyword">$</span> <span class="function">ssh</span> <span class="variable">user@hostinger-vps.com</span>
Welcome to Ubuntu 22.04 LTS

<span class="keyword">user@vps:~$</span> <span class="function">systemctl</span> <span class="variable">status</span> nginx
● nginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running)
     Docs: man:nginx(8)

<span class="keyword">user@vps:~$</span> <span class="function">cat</span> <span class="string">/etc/nginx/sites-available/portfolio</span>
server {
    listen 80;
    server_name sahidafridi.com;
    
    location / {
        root /var/www/portfolio/html;
        index index.html;
        try_files $uri $uri/ =404;
    }
}</code></pre>
                        </div>
                    </div>'''
}

for heading, code_snippet in snippets.items():
    if heading in content:
        # We need to find the bento-content ending for this heading.
        # Find the index of the heading
        idx = content.find(f">{heading}<")
        if idx == -1:
            continue
            
        # Find the closing </div> of bento-content
        end_idx = content.find("</div>", idx)
        if end_idx != -1:
            end_idx += 6 # Include the </div>
            # Check if there is already a code-snippet-bg here
            next_div = content.find("<div", end_idx)
            if next_div != -1 and "code-snippet-bg" in content[next_div:next_div+30]:
                print(f"Skipping {heading}, already has snippet")
                continue
                
            # Insert the snippet after the </div> of bento-content
            content = content[:end_idx] + "\n" + code_snippet + content[end_idx:]

with open(html_path, 'w') as f:
    f.write(content)

print("HTML modified successfully.")
