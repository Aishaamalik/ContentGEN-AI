-- Schema for AI Content Generation Database
-- This creates tables for storing generated content and user feedback

-- Table for storing generated content
CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_type TEXT NOT NULL, -- 'product_description', 'blog_post', 'promotional_copy'
    input_data TEXT NOT NULL, -- JSON string of input parameters
    generated_content TEXT NOT NULL,
    tone TEXT,
    target_audience TEXT,
    platform TEXT, -- For promotional copy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing user feedback on generated content
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    user_feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE
);

-- Table for storing content analytics
CREATE TABLE IF NOT EXISTS analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id INTEGER,
    readability_score REAL,
    sentiment_score REAL,
    sentiment_label TEXT,
    keyword_density REAL,
    word_count INTEGER,
    char_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE
);

-- Index for faster queries
CREATE INDEX IF NOT EXISTS idx_content_type ON content(content_type);
CREATE INDEX IF NOT EXISTS idx_content_created ON content(created_at);
CREATE INDEX IF NOT EXISTS idx_feedback_content ON feedback(content_id);
CREATE INDEX IF NOT EXISTS idx_analytics_content ON analytics(content_id);
