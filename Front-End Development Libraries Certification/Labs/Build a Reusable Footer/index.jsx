function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-brand">
        <span className="footer-badge">FCC Lab</span>
        <h2>Build better projects with reusable UI pieces.</h2>
        <p>
          A flexible footer component with clean spacing, clear navigation, and
          a modern layout.
        </p>
      </div>

      <div className="footer-links">
        <div>
          <h3>Explore</h3>
          <ul>
            <li>
              <a href="#">Challenges</a>
            </li>
            <li>
              <a href="#">Projects</a>
            </li>
          </ul>
        </div>

        <div>
          <h3>Resources</h3>
          <ul>
            <li>
              <a href="#">Docs</a>
            </li>
            <li>
              <a href="#">Guides</a>
            </li>
          </ul>
        </div>

        <div>
          <h3>Connect</h3>
          <ul>
            <li>
              <a href="#">GitHub</a>
            </li>
            <li>
              <a href="#">Community</a>
            </li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom">
        <p>© Made by h-ram on 06 March 2026 At 11:27PM</p>
        <div className="footer-meta-links">
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
          <a href="#">Contact</a>
        </div>
      </div>
    </footer>
  );
}

export { Footer };
