$phpBin = "C:\Users\visha\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.3_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe"
$wpCli = Join-Path $PSScriptRoot "wp-cli.phar"
$wpDir = Join-Path $PSScriptRoot "wordpress"

function Run-WP {
    param([Parameter(ValueFromRemainingArguments=$true)][string[]]$cmdArgs)
    & $phpBin $wpCli --path=$wpDir @cmdArgs
}

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Generating Starter Pages for Your WordPress Website   " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

$pages = @(
    @{ Title = "Home"; Content = "<!-- wp:heading --><h2>Welcome to Our Website</h2><!-- /wp:heading --><!-- wp:paragraph --><p>This is your homepage. You can customize this layout with your favorite blocks, patterns, or Elementor.</p><!-- /wp:paragraph -->" },
    @{ Title = "About Us"; Content = "<!-- wp:heading --><h2>Who We Are</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Share your story, mission, and the team behind your website here.</p><!-- /wp:paragraph -->" },
    @{ Title = "Services"; Content = "<!-- wp:heading --><h2>Our Services</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Detail the solutions, products, and services you provide to your clients.</p><!-- /wp:paragraph -->" },
    @{ Title = "Portfolio"; Content = "<!-- wp:heading --><h2>Featured Work</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Showcase your recent projects, case studies, and achievements.</p><!-- /wp:paragraph -->" },
    @{ Title = "Contact Us"; Content = "<!-- wp:heading --><h2>Get In Touch</h2><!-- /wp:heading --><!-- wp:paragraph --><p>We would love to hear from you. Leave us a message or reach out via email.</p><!-- /wp:paragraph -->" }
)

foreach ($p in $pages) {
    Write-Host "Creating page: $($p.Title)..." -ForegroundColor Yellow
    Run-WP post create --post_type=page --post_title="$($p.Title)" --post_content="$($p.Content)" --post_status="publish"
}

# Set Home as static front page
$homePageId = Run-WP post list --post_type=page --name=home --field=ID
if ($homePageId) {
    Run-WP option update show_on_front "page"
    Run-WP option update page_on_front $homePageId
    Write-Host "Set 'Home' as your static Front Page!" -ForegroundColor Green
}

Write-Host "Starter pages created successfully!" -ForegroundColor Green
