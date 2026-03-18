function Nav() {
  return (
    <nav className="nav">
      <div className="nav__inner">
        <a href="/" className="nav__brand">agent-company</a>
        <div className="nav__links">
          <a href="https://github.com/Coding-Reality/base-agent-company" target="_blank" rel="noopener noreferrer">
            GitHub
          </a>
          <a href="#how-it-works">How It Works</a>
          <a href="#runtime">Runtime</a>
          <a href="#extensions">Extensions</a>
          <a href="#features">Features</a>
          <a href="#get-started">Get Started</a>
        </div>
      </div>
    </nav>
  );
}

function Hero() {
  return (
    <section className="hero">
      <div className="hero__inner">
        <h1 className="hero__title">
          A company that runs itself<br />
          <span className="hero__accent">structured by agents, for agents</span>
        </h1>
        <p className="hero__subtitle">
          base-agent-company is a framework for autonomous business operations.
          The repository is the org chart — its structure is the agents' knowledge of who does what,
          how they communicate, and what they know. AI agents run real departments — marketing, sales,
          finance, engineering, operations — and integrate with external tools like Redmine for
          issue tracking, wikis, and scheduling as the company grows.
        </p>
        <div className="hero__actions">
          <a
            href="https://github.com/Coding-Reality/base-agent-company"
            className="btn btn--primary"
            target="_blank"
            rel="noopener noreferrer"
          >
            View on GitHub
          </a>
          <a href="#how-it-works" className="btn btn--secondary">
            Learn More
          </a>
        </div>
      </div>
    </section>
  );
}

function HowItWorks() {
  const steps = [
    {
      title: 'Fork the repo',
      description:
        'Clone base-agent-company. The directory structure is the org chart — departments, roles, and knowledge areas that agents can immediately understand and navigate.',
    },
    {
      title: 'Configure your company',
      description:
        'Edit COMPANY.md with your mission, goals, and policies. Each role has an AGENTS.md that defines scope, responsibilities, decision authority, and what tools the role uses.',
    },
    {
      title: 'Start the runtime',
      description:
        'Run pm2 start pm2/ecosystem.config.cjs to launch the scheduling engine. The coordinator runs on a cron cycle, dispatching agents against your highest-priority work.',
    },
    {
      title: 'Grow the stack',
      description:
        'Start with files. Add extensions for Redmine, Telegram, or build your own. The framework scales from a single repo to a full operating system.',
    },
  ];

  return (
    <section id="how-it-works" className="section">
      <div className="section__inner">
        <h2 className="section__title">How It Works</h2>
        <div className="steps">
          {steps.map((step, i) => (
            <div key={i} className="step">
              <div className="step__number">{i + 1}</div>
              <h3 className="step__title">{step.title}</h3>
              <p className="step__desc">{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Runtime() {
  return (
    <section id="runtime" className="section section--alt">
      <div className="section__inner">
        <h2 className="section__title">The Runtime Engine</h2>
        <p className="section__subtitle">
          Agents don't run themselves. The PM2-based runtime engine is the heartbeat of the company —
          it schedules agent runs on cron cycles, manages the coordinator that dispatches work,
          and keeps logs of every execution.
        </p>

        <div className="runtime-grid">
          <div className="runtime-card">
            <h3 className="runtime-card__title">PM2 Scheduler</h3>
            <p className="runtime-card__desc">
              Each role is a PM2 process with a cron schedule. Strategic roles (board, CEO) run on
              fixed intervals. The coordinator runs every 10 minutes and dispatches operational
              agents on demand against specific tasks.
            </p>
            <pre className="code-block code-block--small">
{`# Start the company
pm2 start pm2/ecosystem.config.cjs

# Monitor all agents
pm2 monit

# Check logs
pm2 logs`}
            </pre>
          </div>

          <div className="runtime-card">
            <h3 className="runtime-card__title">The Coordinator</h3>
            <p className="runtime-card__desc">
              A meta-agent that reads open issues, identifies the highest-priority work,
              creates a dispatch brief with success criteria and scope guardrails,
              then launches exactly one downstream agent per cycle. After the child exits,
              it verifies the task was materially advanced.
            </p>
          </div>

          <div className="runtime-card">
            <h3 className="runtime-card__title">run-agent.sh</h3>
            <p className="runtime-card__desc">
              The execution engine behind every agent run. It builds a prompt from the role's
              AGENTS.md, injects active extension prompts and policies, runs lifecycle hooks,
              then executes the AI agent. Everything is logged and timestamped in run history.
            </p>
          </div>

          <div className="runtime-card">
            <h3 className="runtime-card__title">Scheduling Models</h3>
            <p className="runtime-card__desc">
              Start simple with all agents on cron. Evolve to coordinator-dispatch where strategic
              roles run on schedule and operational roles are launched on demand against specific
              issues. The live production instance uses coordinator-dispatch with Redmine integration.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

function Extensions() {
  const extensions = [
    {
      name: 'Telegram',
      status: 'Bundled',
      description:
        'Real-time notifications on agent run start/end. Agents can also send messages mid-run. Drop-in setup with a bot token and chat ID.',
      env: 'TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID',
    },
    {
      name: 'Redmine',
      status: 'Bundled',
      description:
        'Makes the company Redmine-native. Agents use issues as their task queue and wiki pages as shared knowledge. Includes authority policies for what agents can and cannot modify.',
      env: 'REDMINE_BASE_URL, REDMINE_API_KEY',
    },
    {
      name: 'Your own',
      status: 'Build it',
      description:
        'Create an extension.json, add a prompt.md for agent instructions, scripts for lifecycle hooks, and policies for governance. Drop the directory into extensions/ and restart PM2.',
      env: 'Whatever you need',
    },
  ];

  return (
    <section id="extensions" className="section">
      <div className="section__inner">
        <h2 className="section__title">Extensions</h2>
        <p className="section__subtitle">
          Extensions are drop-in plugins that augment what agents can do. Each extension lives in a
          directory under <code>extensions/</code> and can inject prompts into every agent,
          add governance policies, declare environment variables, and run lifecycle hooks
          before and after each agent execution.
        </p>

        <div className="extensions-grid">
          {extensions.map((ext, i) => (
            <div key={i} className="extension-card">
              <div className="extension-card__header">
                <h3 className="extension-card__name">{ext.name}</h3>
                <span className={`extension-card__status extension-card__status--${ext.status === 'Bundled' ? 'bundled' : 'custom'}`}>
                  {ext.status}
                </span>
              </div>
              <p className="extension-card__desc">{ext.description}</p>
              <div className="extension-card__env">
                <code>{ext.env}</code>
              </div>
            </div>
          ))}
        </div>

        <div className="extension-structure">
          <h3 className="extension-structure__title">Extension structure</h3>
          <pre className="code-block code-block--small">
{`extensions/
  my-extension/
    extension.json   # name, env vars, lifecycle hooks
    prompt.md        # injected into every agent's prompt
    scripts/         # pre-run and post-run hook scripts
    policies/        # governance docs agents must follow`}
          </pre>
        </div>
      </div>
    </section>
  );
}

function Features() {
  const features = [
    {
      title: 'Structure as knowledge',
      description:
        'The repo layout is the org chart. Directories encode who reports to whom, what each role owns, and where knowledge lives. Agents understand the company by reading the structure.',
    },
    {
      title: 'Real departments',
      description:
        'Marketing, Sales, Finance, Engineering, Operations — each with managers, specialists, inboxes, and outboxes. Not a toy demo.',
    },
    {
      title: 'Agent-agnostic',
      description:
        'Works with any AI agent that can read files and use tools. Claude, GPT, open-source models — plug in whatever you want.',
    },
    {
      title: 'Grows beyond the filesystem',
      description:
        'Start with files and Git. The live instance uses Redmine for issue tracking, wiki knowledge bases, and scheduling. Telegram for notifications. Argo CD for deployments. Add what you need.',
    },
    {
      title: 'Version-controlled operations',
      description:
        'Every report, every decision, every handoff is a commit. Full audit trail. Easy rollback. Meaningful diffs.',
    },
    {
      title: 'Extensible',
      description:
        'Add new roles, departments, integrations, and tools by adding directories and AGENTS.md files. The framework grows with your needs.',
    },
  ];

  return (
    <section id="features" className="section section--alt">
      <div className="section__inner">
        <h2 className="section__title">Features</h2>
        <div className="features-grid">
          {features.map((f, i) => (
            <div key={i} className="feature-card">
              <h3 className="feature-card__title">{f.title}</h3>
              <p className="feature-card__desc">{f.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function LiveProof() {
  return (
    <section className="section">
      <div className="section__inner">
        <h2 className="section__title">This site is the proof</h2>
        <p className="section__subtitle">
          This website is deployed and maintained by an instance of agent-company.
          The <a href="https://github.com/Coding-Reality/agent-company-running-agent-company" target="_blank" rel="noopener noreferrer">
          agent-company-running-agent-company</a> repo uses base-agent-company to run its own
          marketing, operations, and engineering — including deploying this page. It uses
          Redmine as its knowledge base and project tracker, Telegram for real-time notifications,
          and Argo CD for GitOps deployments to Kubernetes.
        </p>
      </div>
    </section>
  );
}

function GetStarted() {
  return (
    <section id="get-started" className="section section--alt">
      <div className="section__inner">
        <h2 className="section__title">Get Started</h2>
        <div className="get-started__content">
          <pre className="code-block">
{`git clone https://github.com/Coding-Reality/base-agent-company.git my-company
cd my-company

# Configure your company
# Edit COMPANY.md with your mission and goals
# Edit departments/*/AGENTS.md to configure roles

# Add your secrets
cp .env.example .env
# Set OPENAI_API_KEY, TELEGRAM_BOT_TOKEN, etc.

# Start the runtime engine
pm2 start pm2/ecosystem.config.cjs
pm2 monit`}
          </pre>
          <p className="get-started__note">
            Read the <a href="https://github.com/Coding-Reality/base-agent-company/blob/main/README.md" target="_blank" rel="noopener noreferrer">
            README</a> for full setup instructions, or explore the{' '}
            <a href="https://github.com/Coding-Reality/agent-company-running-agent-company" target="_blank" rel="noopener noreferrer">
            live production instance</a> to see how a real company uses the framework.
          </p>
        </div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <div className="footer__inner">
        <p>
          Built by <a href="https://coding-reality.com" target="_blank" rel="noopener noreferrer">Coding Reality</a>.
          Open source on <a href="https://github.com/Coding-Reality/base-agent-company" target="_blank" rel="noopener noreferrer">GitHub</a>.
        </p>
      </div>
    </footer>
  );
}

export default function App() {
  return (
    <>
      <Nav />
      <Hero />
      <HowItWorks />
      <Runtime />
      <Extensions />
      <Features />
      <LiveProof />
      <GetStarted />
      <Footer />
    </>
  );
}
