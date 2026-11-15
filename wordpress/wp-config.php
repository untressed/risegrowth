<?php
/**
 * The base configuration for WordPress
 */

// Database settings - SQLite driver intercepts these if db.php is present, or uses MySQL if MySQL credentials are set.
define( 'DB_NAME', 'wordpress' );
define( 'DB_USER', 'root' );
define( 'DB_PASSWORD', '' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', '' );

/** Authentication unique keys and salts. */
define('AUTH_KEY',         '[x@GUV<mvds/JetN.UP>.iF&:8h-+<~e[Hy?M-VGV-GYYZ>LS)12:6/.%F6#T+F&');
define('SECURE_AUTH_KEY',  's%x6h>12!jSE[>X]@ej)=}!O{+7-eWPLg;j>@MC@>b$1VG^W:A}k0|&YR~gAtGUB');
define('LOGGED_IN_KEY',    '0Awkz4DBmn_Zw_b!u+$p}I-&/6q/su}]D7xsqWr|(X<p8-vhJ0>,Q^aU#;|JptM=');
define('NONCE_KEY',        'Nn*<Cl6|+S Qicg3{vIyZJ1|f#X3 6{cxg|3_3HgOoo`eDZES<*6Ow6t:Z[8)qnz');
define('AUTH_SALT',        'Y23h+ZXMGf/Jr-bJ-(PyCH~+K#p^9T2s-av/;<!S^J>v<(RjVLRFgP|F^|#[8Wwh');
define('SECURE_AUTH_SALT', 'cUh,gU&X(|$WYGOK#>+eS@xs9~9-sFvOZubhtP)[xz6&FTq{~2R,CyrpG@t]0dC5');
define('LOGGED_IN_SALT',   '$7[WZ?X*Shr0WEl0~&5>C1q1JrytFuVQS(M2OA@6B `&`{4:s$1 b-*R{=)QCik5');
define('NONCE_SALT',       'G~SHNx,i+hFa-UA{JN+=>]a|,oS]Xv`vN5BA8wIw{<#yb+XDj[hg?8/)~<d7P@Vv');

$table_prefix = 'wp_';

define( 'WP_DEBUG', false );

// Direct filesystem method for local plugin/theme installation without FTP prompts
define( 'FS_METHOD', 'direct' );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
