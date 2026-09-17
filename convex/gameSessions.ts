import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const get = query({
  args: { sessionId: v.string() },
  returns: v.union(v.object({ state: v.any(), updatedAt: v.number() }), v.null()),
  handler: async (ctx, { sessionId }) => {
    const row = await ctx.db
      .query("gameSessions")
      .withIndex("by_session", (q) => q.eq("sessionId", sessionId))
      .unique();
    return row ? { state: row.state, updatedAt: row.updatedAt } : null;
  },
});

export const save = mutation({
  args: {
    sessionId: v.string(),
    state: v.any(),
    updatedAt: v.number(),
  },
  returns: v.null(),
  handler: async (ctx, { sessionId, state, updatedAt }) => {
    const existing = await ctx.db
      .query("gameSessions")
      .withIndex("by_session", (q) => q.eq("sessionId", sessionId))
      .unique();

    if (existing) {
      await ctx.db.patch(existing._id, { state, updatedAt });
    } else {
      await ctx.db.insert("gameSessions", { sessionId, state, updatedAt });
    }
    return null;
  },
});
