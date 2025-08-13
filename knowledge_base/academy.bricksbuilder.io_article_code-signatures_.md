---
title: "Code signatures – Bricks Academy"
url: https://academy.bricksbuilder.io/article/code-signatures/
date: 2025-02-27T15:30:37.149831
status: success
---

# Code signatures – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/code-signatures/](https://academy.bricksbuilder.io/article/code-signatures/)*

## Table of Contents

- [Code signatures](#code-signatures)
  - [Elements that require code signatures](#elements-that-require-code-signatures)
  - [How to generate code signatures](#how-to-generate-code-signatures)
    - [Generate code signatures in the builder](#generate-code-signatures-in-the-builder)
      - [Sign code for an individual element](#sign-code-for-an-individual-element)
    - [View & sign unsigned code in bulk](#view--sign-unsigned-code-in-bulk)
    - [Sign all code globally via Bricks settings](#sign-all-code-globally-via-bricks-settings)
  - [Locking code signature generation](#locking-code-signature-generation)
  - [When to regenerate signatures](#when-to-regenerate-signatures)
  - [Why code signatures?](#why-code-signatures)
    - [Understanding WordPress salts](#understanding-wordpress-salts)
    - [Understanding thewp_hashfunction](#understanding-thewphashfunction)
    - [Bricks code integrity verification process](#bricks-code-integrity-verification-process)
        - [Query Sort, Filter & Live Search](#query-sort-filter--live-search)
        - [Code review](#code-review)

## Code signatures

With the release of version 1.9.7, Bricks takes another significant step to enhance the built-in code security by introducing code signatures.

Code signatures ensure that the code you are running has not been tampered with. Valid code signatures are now mandatory. Any code without a valid signature won’t run.

### Elements that require code signatures

The following elements require valid code signatures to run:

- Code element with “Code execution” enabled
- SVG element with “Source” set to “Code”
- Query loop editor

### How to generate code signatures

You can generate code signatures for individual elements when editing them in the builder, for the entire page inside the builder, or globally via the Bricks settings. Let’s explore all options together.

#### Generate code signatures in the builder

Inside the builder, all elements with unsigned code are highlighted in red. You’ll also see a red “fingerprint” icon at the top of the structure panel.

##### Sign code for an individual element

To generate a code signature for an individual element while you edit it, you can click the “Sign code” button right above the code editor. Or, if your cursor focus is inside the code editor, use the “CMD/CRTL + R” keyboard shortcut.

#### View & sign unsigned code in bulk

You can also view and sign all elements with unsigned code on the current page by clicking the “fingerprint” icon at the top of the structure panel. The same icon is also available on individual unsigned elements in the structure panel.

#### Sign all code globally via Bricks settings

To generate code signatures for your entire site, navigate toBricks > Settings> Custom code > Code signature in your WordPress dashboard.

`Bricks > Settings`

Click theRegenerate code signaturesbutton. This will generate code signatures for all pages, templates, etc., built with Bricks.

`Regenerate code signatures`

This feature is only available when code execution is enabled and for users with code execution capability.

### Locking code signature generation

In Bricks 1.11.1, we introduced theBRICKS_LOCK_CODE_SIGNATURESconstant, an additional layer of control for high-security environments. WhenBRICKS_LOCK_CODE_SIGNATURESis set totrue, Bricks prevents any new code signatures from being generated, regardless of user permissions. This feature is especially useful if you want to lock down the ability to modify code signatures after initial development is complete.

`BRICKS_LOCK_CODE_SIGNATURES`

`BRICKS_LOCK_CODE_SIGNATURES`

`true`

To enable this lock, add the following line to yourfunctions.phpfile:

`functions.php`

```
if ( ! defined( 'BRICKS_LOCK_CODE_SIGNATURES' ) ) {
    define( 'BRICKS_LOCK_CODE_SIGNATURES', true );
}
```

`if ( ! defined( 'BRICKS_LOCK_CODE_SIGNATURES' ) ) {
    define( 'BRICKS_LOCK_CODE_SIGNATURES', true );
}`

With this constant set totrue, any attempt to generate new code signatures will be blocked. This constant provides an alternative to the Bricks settings for managing code signature access in production environments where strict security is essential.

`true`

### When to regenerate signatures

When updating Bricks from a version before 1.9.7, generating code signatures viaBricks > Settingsfor your code to execute is mandatory, as only code with a valid signature will be executed. Please make sure to first perform a “Code review” on the same page.

`Bricks > Settings`

After changing your WordPress salt (secret keys):Whenever the salts inwp-config.phpare changed, you have to regenerate code signatures.

`wp-config.php`

After site migration:When moving your site to a new domain or server, you might need to regenerate signatures if the salts in the new environment are different.

### Why code signatures?

Before explaining the rationale behind introducing code signatures in Bricks and how Bricks uses them, it’s important to understand how hashing works and the specific role of WordPress salts in this process.

#### Understanding WordPress salts

In the context of WordPress, salts are essentially random strings that serve as keys for cryptographic operations.

These strings, stored in thewp-config.phpfile, are crucial for operations like keyed hashing and encryption. Salts add an extra layer of security by ensuring that the hash signatures generated for your site’s code are unique and securely encrypted.

`wp-config.php`

In simpler terms, think of WordPress salts as a secret ingredient in your website’s recipe, stored in thewp-config.phpfile. Just like a secret ingredient can uniquely identify a dish, these salts ensure the uniqueness of your website’s code.

`wp-config.php`

When the code is prepared (or hashed) with this secret ingredient, it creates a signature that’s unique to your site.

If someone tries to replicate or alter your website’s code without knowing the secret ingredient, their version won’t have the same signature, making it easy to spot and reject the change.

#### Understanding thewp_hashfunction

`wp_hash`

For hashing, Bricks utilizes the WordPress-nativewp_hashfunction, which uses an HMAC-MD5 algorithm to generate unique hash signatures.

`wp_hash`

This function combines your site’s data with its unique salts, creating a hash signature that is distinctive to your site.

#### Bricks code integrity verification process

In Bricks, these hash signatures are important in ensuring that any modifications to the code on your site can only be made with access to these unique salts and code execution capability in Bricks.

Here’s a brief overview of how this process works:

1. Code and signature generation:When you sign your code, a unique hash signature is generated using your site’s unique WordPress salts.
2. Code retrieval for execution:When the code is accessed on your site, Bricks retrieves the code and its stored hash signature from the database.
3. Verification process:Bricks re-hashes the retrieved code and compares this new hash with the original stored signature.
4. Execution decision:If the hashes match, it confirms the code’s integrity, allowing it to execute. A mismatch indicates potential unauthorized changes, preventing execution.

The integration ofCode signatures&Code reviewin Bricks 1.9.7 marks a significant advancement in our commitment to enhancing the security and integrity of websites built with Bricks.

`Code signatures`

`Code review`

Collectively, these enhancements provide a comprehensive framework for ensuring the security and authenticity of your site’s code. Helping you safeguard against potential unauthorized modifications and maintain the overall health and safety of your WordPress site.

###### Query Sort, Filter & Live Search

###### Code review

