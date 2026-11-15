<?php
/**
 * Rise Growth Group — Custom Post Types & REST Meta Registration
 * Registers all CPTs with show_in_rest: true so React can consume them.
 */

add_action( 'init', 'rise_register_cpts' );
function rise_register_cpts() {

    /* ── 1. SERVICES ─────────────────────────────────────────── */
    register_post_type( 'rise_service', [
        'labels'       => [ 'name' => 'Services', 'singular_name' => 'Service' ],
        'public'       => true,
        'show_in_rest' => true,
        'rest_base'    => 'services',
        'supports'     => [ 'title', 'editor', 'excerpt', 'custom-fields' ],
        'menu_icon'    => 'dashicons-chart-line',
    ]);

    /* ── 2. TEAM MEMBERS ─────────────────────────────────────── */
    register_post_type( 'rise_team', [
        'labels'       => [ 'name' => 'Team Members', 'singular_name' => 'Team Member' ],
        'public'       => true,
        'show_in_rest' => true,
        'rest_base'    => 'team',
        'supports'     => [ 'title', 'editor', 'excerpt', 'custom-fields' ],
        'menu_icon'    => 'dashicons-groups',
    ]);

    /* ── 3. TESTIMONIALS ─────────────────────────────────────── */
    register_post_type( 'rise_testimonial', [
        'labels'       => [ 'name' => 'Testimonials', 'singular_name' => 'Testimonial' ],
        'public'       => true,
        'show_in_rest' => true,
        'rest_base'    => 'testimonials',
        'supports'     => [ 'title', 'editor', 'excerpt', 'custom-fields' ],
        'menu_icon'    => 'dashicons-format-quote',
    ]);

    /* ── 4. FAQS ─────────────────────────────────────────────── */
    register_post_type( 'rise_faq', [
        'labels'       => [ 'name' => 'FAQs', 'singular_name' => 'FAQ' ],
        'public'       => true,
        'show_in_rest' => true,
        'rest_base'    => 'faqs',
        'supports'     => [ 'title', 'editor', 'custom-fields' ],
        'menu_icon'    => 'dashicons-editor-help',
    ]);
}

add_action( 'rest_api_init', 'rise_register_meta_fields' );
function rise_register_meta_fields() {

    $default_args = [
        'show_in_rest' => true,
        'single'       => true,
        'type'         => 'string',
        'auth_callback' => '__return_true',
    ];

    /* ── SERVICE meta ─────────────────────────────────────────── */
    foreach ( [ 'rise_icon', 'rise_color', 'rise_border_color', 'rise_filter_id', 'rise_features' ] as $key ) {
        register_post_meta( 'rise_service', $key, $default_args );
    }

    /* ── TEAM meta ────────────────────────────────────────────── */
    foreach ( [ 'rise_role', 'rise_initials', 'rise_bg_gradient' ] as $key ) {
        register_post_meta( 'rise_team', $key, $default_args );
    }

    /* ── TESTIMONIAL meta ─────────────────────────────────────── */
    foreach ( [ 'rise_role', 'rise_initials', 'rise_bg_gradient', 'rise_rating' ] as $key ) {
        register_post_meta( 'rise_testimonial', $key, $default_args );
    }
}
