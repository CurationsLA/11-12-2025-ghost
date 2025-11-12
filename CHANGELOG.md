# CurationsLA Newsletter Theme Changelog

## Version 10.5.1-ULTIMATE-ENHANCED

### 🐛 Bug Fixes
- **FIXED**: Ghost theme error - Unused custom theme settings
  - Now using `@custom.newsletter_accent_color` in footer template
  - Now using `@custom.show_newsletter_signup` in error page template
- **FIXED**: All custom theme settings are now properly utilized in templates

## Version 10.5.0-ULTIMATE-ENHANCED

### 🐛 Bug Fixes
- **FIXED**: Ghost theme error - Missing custom theme setting `newsletter_accent_color`
  - Updated `partials/universal-footer-tagline.hbs` to use `@custom.accent_color`
  - Added backward compatibility setting for `newsletter_accent_color`

### ✨ Enhancements
- **NEW**: Added customizable footer text setting
- **NEW**: Added customizable brand URL setting  
- **NEW**: Added newsletter signup toggle setting
- **IMPROVED**: Enhanced footer template with conditional logic
- **IMPROVED**: Better theme customization options in Ghost admin

### 🔧 Technical Improvements
- All custom theme settings properly defined in package.json
- Enhanced backward compatibility
- Improved theme configuration structure
- Version bump to 10.5.1-ULTIMATE-ENHANCED

### 📧 Email Template
- Maintained all existing email styling functionality
- No breaking changes to newsletter layout
- Full Ghost 6.0+ compatibility maintained

---
**A project curated by Humans x AI at Curations.cc**