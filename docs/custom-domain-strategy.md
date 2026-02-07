# Custom Domain Strategy

Decision notes on GitHub Pages domain for the book site.

---

## Current Setup

- **GitHub Pages URL:** `https://saurav-yirifi.github.io/blueprint-ai-first-company/`
- **Config:** `mkdocs.yml` `site_url` field
- **Repo:** `saurav-yirifi/blueprint-ai-first-company`

## Recommendation: Use a Custom Domain

A custom domain wins for discovery, branding, and long-term SEO ownership.

### github.io: Free Domain Authority, Zero Brand Equity

| Pros | Cons |
|------|------|
| GitHub's domain authority (~95/100) gives immediate ranking boost | You build SEO equity for `github.io`, not your brand |
| Zero setup, free HTTPS | URL looks like a side project, not a product |
| New pages can rank faster initially | If you move off GitHub Pages, you lose all ranking |
| | Google may treat it as developer docs, not an authoritative book site |

### Custom Domain: Slower Start, Permanent Asset

| Pros | Cons |
|------|------|
| You own the ranking equity forever -- it compounds | New domain starts with zero authority (3-6 months to build) |
| Branded URL is memorable and shareable | Costs ~$12/year for a standalone domain |
| Better CTR in search results -- people click branded domains more | |
| Cross-links between blog, Yirifi, and book site reinforce each other's authority | |
| Canonical authority is yours -- no risk of Google preferring github.io | |

## Domain Options

| Option | URL | Cost | Notes |
|--------|-----|------|-------|
| Subdomain of yirifi.ai | `blueprint.yirifi.ai` | Free | Inherits yirifi.ai domain authority immediately. Ties book to company brand. Fastest path. |
| Standalone domain | `blueprintaifirst.com` | ~$12/year | Independent brand, but starts from zero authority. Better if the book should stand alone from Yirifi. |
| Keep github.io | `saurav-yirifi.github.io/blueprint-ai-first-company/` | Free | No brand equity. Looks like a developer project. |

**Recommended:** `blueprint.yirifi.ai` -- inherits existing domain authority, costs nothing extra, ties the book to the company brand.

## Implementation Steps

1. **DNS:** Add a CNAME record pointing `blueprint.yirifi.ai` to `saurav-yirifi.github.io`
2. **GitHub:** In repo Settings > Pages, set custom domain to `blueprint.yirifi.ai`
3. **HTTPS:** GitHub auto-issues a Let's Encrypt certificate once DNS propagates
4. **mkdocs.yml:** Update `site_url` to `https://blueprint.yirifi.ai/`
5. **CNAME file:** GitHub creates this automatically, or add `docs/CNAME` with the domain
6. **Google Search Console:** Submit the new domain and sitemap (`/sitemap.xml`)
7. **Canonical URLs:** MkDocs handles this via `site_url` -- no extra config needed
8. **Old URL:** GitHub automatically redirects `saurav-yirifi.github.io/blueprint-ai-first-company/` to the custom domain

## SEO Checklist After Custom Domain

- [ ] Verify domain in Google Search Console
- [ ] Submit sitemap.xml
- [ ] Confirm HTTPS is enforced (GitHub Pages setting)
- [ ] Update all external links (README, social profiles, blog) to use the custom domain
- [ ] Add `<meta>` descriptions via MkDocs page metadata where relevant
- [ ] Cross-link from blog.sauravbhatia.com and yirifi.ai to the book site

## References

- [GitHub Docs: Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub SEO Guide 2025](https://www.gitdevtool.com/blog/github-seo)
- [Mastering SEO for GitHub Pages](https://www.jekyllpad.com/blog/mastering-github-pages-seo-7)
- [Optimizing SEO for GitHub-Hosted Sites](https://free-git-hosting.github.io/seo-for-github-hosted-sites/)
