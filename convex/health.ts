import { query } from "./_generated/server";

export const check = query({
  args: {},
  handler: async () => ({
    app: "Fysioverse",
    status: "online",
    purpose: "education-simulation-backend",
  }),
});
