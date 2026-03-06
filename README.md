# pyDQT - Python Dynamic Quantity Takeoff for Revit

Professional BIM Automation Tools Suite for Revit Model Management and Optimization.

## Features

- 🔧 **20+ Specialized Revit Automation Tools**
- 📊 **Advanced Model Health Analysis**
- 🏗️ **Comprehensive BIM Cleanup & Management**
- 📈 **Schedule Export/Import with Excel Integration**
- 🎨 **Professional DQT-branded UI Components**
- ✅ **IFC-SG & AIM Submission Ready**
- 🔐 **Safety-first Design with Confirmation Dialogs**

## Quick Start

1. Download the latest release
2. Extract to PyRevit Extensions folder:
   ```
   %APPDATA%\pyRevit\Extensions\
   ```
3. Restart Revit
4. Access tools via **Add-Ins > pyDQT**

## Tools Overview

### Data Management
- **Contains Manager** - Find elements in rooms/areas/spaces
- **IFC-SG Checker** - Validate IFC Submission Grade compliance
- **Model Checker** - Comprehensive model health analysis
- **Schedule Export/Import** - Bidirectional Excel integration

### Inquiry & Analysis
- **Health Check** - Detect model issues
- **Quick Element** - Fast element selection tools
- **Sheet Manager** - Advanced sheet management
- **View Manager** - View organization and optimization

### Geometry Tools
- **Tag Leader Straightener** - Orthogonal leader formatting
- **Room to Area Converter** - Dynamic conversion with parameter filtering
- **Grid/Level Alignment** - Align datum elements precisely
- **Wall/Column/Floor Split** - Geometric element division

### Purge & Cleanup
- **Advanced Purge** - Granular deletion control
- **Smart Purge** - Intelligent cleanup with dependency checking
- **Smart Delete** - Safe element removal

## System Requirements

- **Revit** 2019 or later
- **PyRevit** 4.5 or later
- **Python** 3.7+
- **Windows** 10/11

## Documentation

- [Installation Guide](docs/installation.md)
- [User Guide](docs/user-guide.md)
- [Feature Documentation](docs/features/)
- [API Reference](docs/api-reference.md)

## Architecture

```
pyDQT/
├── src/pyDQT/
│   ├── shared/          # Reusable components
│   ├── tools/           # Tool implementations
│   └── utils/           # Utility functions
├── resources/           # Icons, configs, templates
├── docs/                # Documentation
└── tests/               # Unit tests
```

## Key Principles

✨ **Safety First** - All destructive operations require explicit user confirmation
🔧 **Reliability** - Thoroughly tested in production environments
📚 **Documentation** - Comprehensive guides for every tool
🎨 **Consistency** - Unified UI across all tools with branded colors
♻️ **Reusability** - Shared library architecture reduces code duplication

## Support

- 📧 Issues & Feedback: [GitHub Issues](https://github.com/yourusername/pyDQT/issues)
- 💡 Feature Requests: [GitHub Discussions](https://github.com/yourusername/pyDQT/discussions)

## License

MIT License - See [LICENSE](LICENSE) file for details

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](.github/CONTRIBUTING.md)

---

**Made for the AEC Community** | Simplifying BIM Automation
