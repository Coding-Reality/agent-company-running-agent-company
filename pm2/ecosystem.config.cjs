const path = require("path");
const fs = require("fs");

const root = path.resolve(__dirname, "..");

// Load .env from project root
const envFile = path.join(root, ".env");
if (fs.existsSync(envFile)) {
  for (const line of fs.readFileSync(envFile, "utf8").split("\n")) {
    const match = line.match(/^\s*([^#=]+?)\s*=\s*(.*)\s*$/);
    if (match && !process.env[match[1]]) process.env[match[1]] = match[2];
  }
}

const runAgent = (name, cron) => ({
  name,
  cwd: root,
  script: "/bin/bash",
  args: ["-lc", `${path.join(root, "scripts/run-agent.sh")} ${name}`],
  autorestart: false,
  cron_restart: cron,
  time: true,
  out_file: path.join(root, "runtime/logs", `${name.replace(/\//g, "_")}.out.log`),
  error_file: path.join(root, "runtime/logs", `${name.replace(/\//g, "_")}.err.log`),
  merge_logs: true,
  env: {
    AGENT_COMPANY_ROOT: root,
    AGENT_NAME: name,
    OPENAI_API_KEY: process.env.OPENAI_API_KEY,
    TELEGRAM_BOT_TOKEN: process.env.TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID,
    REDMINE_BASE_URL: process.env.REDMINE_BASE_URL,
    REDMINE_API_KEY: process.env.REDMINE_API_KEY,
  },
});

module.exports = {
  apps: [
    runAgent("board/chair", "0 */4 * * *"), // run every 4 hours for strategic oversight
    runAgent("board/strategy-member", "10 */4 * * *"), // run every 4 hours, 10 min after chair
    runAgent("executive/ceo", "*/15 * * * *"), // run every 15 minutes to coordinate execution
    runAgent("departments/sales/manager", "3,18,33,48 * * * *"), // run every 15 minutes, offset from CEO
    runAgent("departments/sales/outbound-1", "*/10 * * * *"), // run every 10 minutes for aggressive outreach
    runAgent("departments/marketing/manager", "5,20,35,50 * * * *"), // run every 15 minutes, offset
    runAgent("departments/marketing/content", "0,30 * * * *"), // run every 30 minutes for content waves
    runAgent("departments/operations/manager", "8,23,38,53 * * * *"), // run every 15 minutes for ops review
    runAgent("departments/research/market-intel", "0 * * * *"), // run every hour for market intel
    runAgent("departments/finance/manager", "0 */2 * * *"), // run every 2 hours for financial review
    runAgent("departments/engineering/ai-engineer", "30 * * * *"), // run every hour for context engineering audits
  ],
};
