import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  gameSessions: defineTable({
    sessionId: v.string(),
    state: v.any(),
    updatedAt: v.number(),
  }).index("by_session", ["sessionId"]),
});
