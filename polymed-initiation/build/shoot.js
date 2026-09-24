// Usage: node build/shoot.js <html> <outprefix> [width] [--full]
const { chromium } = require('playwright');
(async () => {
  const [html, out, width = '1280', full] = process.argv.slice(2);
  const browser = await chromium.launch();
  for (const theme of ['light', 'dark']) {
    const page = await browser.newPage({ viewport: { width: parseInt(width), height: 1000 }, colorScheme: theme });
    await page.goto('file://' + require('path').resolve(html));
    await page.screenshot({ path: `${out}_${theme}.png`, fullPage: full === '--full' });
    await page.close();
  }
  await browser.close();
})();
