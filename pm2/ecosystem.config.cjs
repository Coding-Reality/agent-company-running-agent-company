const path = require("path");

const root = path.resolve(__dirname, "..");

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
    TELEGRAM_BOT_TOKEN: process.env.TELEGRAM_BOT_TOKEN || "8756615608:AAHJo5tumHu9v2xOLHuTtvXughgqN-VWYvI",
    TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID || "5287235587",
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
  ],
};
