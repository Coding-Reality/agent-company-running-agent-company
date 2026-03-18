import { useState } from 'react';

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
      title: 'Run agents',
      description:
        'Point AI agents at roles. They read their instructions, check inboxes, do work, write reports, and coordinate through the filesystem and integrated tools.',
    },
    {
      title: 'Grow the stack',
      description:
        'Start with files. Add Redmine for issue tracking and wikis, Telegram for notifications, CI/CD for deployments. The framework scales from a single repo to a full operating system.',
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
# Edit COMPANY.md with your mission
# Edit departments/*/AGENTS.md to configure roles
# Point your AI agents at the roles and run them`}
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
      <Features />
      <LiveProof />
      <GetStarted />
      <Footer />
    </>
  );
}
