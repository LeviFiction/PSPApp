
class APP:
    TargetDocument = None
    ActiveDocument = None
    def __init__(self):
        self.Documents = []
        self.TargetDocument = self.PSPDocument()
        self.ActiveDocument = self.PSPDocument()
        self.Constants = self.PSPConstantPool([])
        pass
    
    def Do(self, Environment, command, d={}, doc = None):
        strReturns =  ['SelectLayer', 'SelectPreviousTool', 'SelectTool', 'SelectNextTool'] 
        dictReturns = ['GetCommandInfo', 'GetMaterial', 'GetNextObject', 'GetNumber', 'GetPrevObject', 'GetRasterSelectionRect', 'GetString', 'GetVectorSelectionRect', 'GetVersionInfo', 'ReturnFileLocations', 'ReturnGeneralPreferences', 'ReturnImageInfo', 'ReturnLayerProperties', 'ReturnVectorObjectProperties', "ImageQualityCheck"] 
        listReturns = ['FileAssociations'] 
        boolReturns =  ['CompareCheckpoints', 'HasVectorSelection', 'ScriptSingleStep', 'ScriptWndAutoShow', 'SelectNextLayer', 'SelectPreviousLayer', 'RestoreOriginalFile', 'RestoreOriginalImage'] 
        intReturns =  ['CountColors', 'CountImageColors', 'FileOpen', 'MsgBox', 'ScriptWndFilterLevel'] 

        if command in dictReturns:
            return dict
        elif command in listReturns:
            return list
        elif command in strReturns:
            return str
        elif command in boolReturns:
            return bool
        elif command in intReturns:
            return int
        else:
            return None

    def __getitem__(self, key):
        pass
    def EndMemStats(self):
        pass
    def GetCommandParameters(self):
        pass
    def GetMemStats(self):
        pass
    def StartMemStats(self):
        pass
    
    class PSPDocument:
        def __init__(self):
            self.Width = 0
            self.Height = 0
            self.Name = ""
            self.Title = ""

    class PSPConstantPool():
        '''PSPConstantPool is a holder for a list of all constants in PSPEnumType'''
        class PSPEnumType:
            __Description = ""
            __Name = ""
            __Values = []
            def __init__(self, Description = "", Name = "", Values = []):
                self.__Description = Description
                self.__Name = Name
                self.__Values = Values
                pass
            def Description(self):
                return self.__Description
            def Name(self):
                return self.__Name
            def Values(self):
                return self.__Values
            def __getattr__(self, key):
                for x in self.__Values:
                    if key == x[0]:
                        return x[1]

        class __SeamCarvingActionConst(PSPEnumType): 
            '''SeamCarvingAction'''
            HResize = 0
            HScale = 1
            HRemove = 2
            VResize = 3
            VScale = 4
            VRemove = 5
            Fusion = 6
            def __init__(self):
                self.__name = "SeamCarvingAction"
                self.__desc = "SeamCarvingAction"
                self.__values = [("HResize", 0, ""),("HScale", 1, ""),("HRemove", 2, ""),("VResize", 3, ""),("VScale", 4, ""),("VRemove", 5, ""),("Fusion", 6, ""),]


        class __HDPVariantConst(PSPEnumType): 
            '''HDPVariant'''
            Lossy = 0
            Lossless = 1
            def __init__(self):
                self.__name = "HDPVariant"
                self.__desc = "HDPVariant"
                self.__values = [("Lossy", 0, ""),("Lossless", 1, ""),]


        class __PhotoLookEffectConst(PSPEnumType): 
            '''Photo Look Effect'''
            EffectNone = 0
            Vivid = 1
            VividSkin = 2
            MutedReds = 3
            EnhancedReds = 4
            VibrantFoliage = 5
            WarmEarth = 6
            Glamour = 7
            def __init__(self):
                self.__name = "PhotoLookEffect"
                self.__desc = "Photo Look Effect"
                self.__values = [("EffectNone", 0, "None"),("Vivid", 1, "Vivid"),("VividSkin", 2, "Vivid skin tones"),("MutedReds", 3, "Muted reds"),("EnhancedReds", 4, "Enhanced reds"),("VibrantFoliage", 5, "Vibrant foliage"),("WarmEarth", 6, "Warm earth tones"),("Glamour", 7, "Glamour"),]


        class __keImageQualityConst(PSPEnumType): 
            '''keImageQuality'''
            keLow = 0
            keMedium = 1
            keBest = 2
            def __init__(self):
                self.__name = "keImageQuality"
                self.__desc = "keImageQuality"
                self.__values = [("keLow", 0, ""),("keMedium", 1, ""),("keBest", 2, ""),]


        class __OptimizedSizeConst(PSPEnumType): 
            '''OptimizedSize'''
            Small = 0
            Medium = 1
            Large = 2
            CellPhone1 = 3
            CellPhone2 = 4
            CellPhone3 = 5
            def __init__(self):
                self.__name = "OptimizedSize"
                self.__desc = "OptimizedSize"
                self.__values = [("Small", 0, ""),("Medium", 1, ""),("Large", 2, ""),("CellPhone1", 3, "The Makeover tool's subtool."),("CellPhone2", 4, "Selects the Blemish Fixer subtool"),("CellPhone3", 5, "Selects the Toothbrush subtool"),]


        class __MakeoverModeConst(PSPEnumType): 
            '''The Makeover tool's subtool.'''
            BlemishFixer = 0
            Toothbrush = 1
            Suntan = 2
            EyeDrop = 3
            Thinify = 4
            def __init__(self):
                self.__name = "MakeoverMode"
                self.__desc = "The Makeover tool's subtool."
                self.__values = [("BlemishFixer", 0, "Selects the Blemish Fixer subtool"),("Toothbrush", 1, "Selects the Toothbrush subtool"),("Suntan", 2, "Selects the Suntan subtool"),("EyeDrop", 3, "Selects the Eye Drops tool"),("Thinify", 4, "Selects the Thinify tool"),]


        class __PolarDirectionConst(PSPEnumType): 
            '''Specifies how polar coordinates effect will be applied to the image or selection.'''
            RectToPolar = 0
            PolarToRect = 1
            def __init__(self):
                self.__name = "PolarDirection"
                self.__desc = "Specifies how polar coordinates effect will be applied to the image or selection."
                self.__values = [("RectToPolar", 0, "Transform from rectangular to polar coordinates."),("PolarToRect", 1, "Transform from polar to rectangular coordinates."),]


        class __MaterialStyleConst(PSPEnumType): 
            '''Defines the style type for a material.'''
            Color = 0
            Gradient = 1
            Pattern = 2
            def __init__(self):
                self.__name = "MaterialStyle"
                self.__desc = "Defines the style type for a material."
                self.__values = [("Color", 0, "Style type is a solid color"),("Gradient", 1, "Style type is a gradient"),("Pattern", 2, "Style type is a pattern"),]


        class __EyeColorConst(PSPEnumType): 
            '''Color of the eye'''
            Aqua = 0
            Blue = 1
            Brown = 2
            Gray = 3
            Green = 4
            Violet = 5
            def __init__(self):
                self.__name = "EyeColor"
                self.__desc = "Color of the eye"
                self.__values = [("Aqua", 0, "Aqua"),("Blue", 1, "Blue"),("Brown", 2, "Brown"),("Gray", 3, "Grey"),("Green", 4, "Green"),("Violet", 5, "Violet"),]


        class __DeformationMapFormatConst(PSPEnumType): 
            '''Deformation Map format ( PaintShop Pro, Photoshop Liquify )'''
            PaintShopPro = 0
            PhotoshopLiquify = 1
            def __init__(self):
                self.__name = "DeformationMapFormat"
                self.__desc = "Deformation Map format ( PaintShop Pro, Photoshop Liquify )"
                self.__values = [("PaintShopPro", 0, "map format is PaintShop Pro"),("PhotoshopLiquify", 1, "map format is Photoshop Liquify"),]


        class __JascFileFormatsConst(PSPEnumType): 
            '''File format codes '''
            JID_FORMAT_NOINFO = -1
            JID_FORMAT_UNKNOWN = 0
            JID_FORMAT_AFX = 1
            JID_FORMAT_BMP = 2
            JID_FORMAT_BRK = 3
            JID_FORMAT_CAL = 4
            JID_FORMAT_CGM = 5
            JID_FORMAT_CISRLE = 6
            JID_FORMAT_CLP = 7
            JID_FORMAT_CUR = 8
            JID_FORMAT_CUT = 9
            JID_FORMAT_DCX = 10
            JID_FORMAT_DGN = 11
            JID_FORMAT_DIB = 12
            JID_FORMAT_DWG = 13
            JID_FORMAT_EMF = 14
            JID_FORMAT_EPS = 15
            JID_FORMAT_FPX = 16
            JID_FORMAT_FSP = 17
            JID_FORMAT_GIF = 18
            JID_FORMAT_ICO = 19
            JID_FORMAT_IFF = 20
            JID_FORMAT_IMG = 21
            JID_FORMAT_JIF = 22
            JID_FORMAT_JP2 = 23
            JID_FORMAT_JPG = 24
            JID_FORMAT_KDC = 25
            JID_FORMAT_KFX = 26
            JID_FORMAT_LBM = 27
            JID_FORMAT_LPIC = 28
            JID_FORMAT_LV = 29
            JID_FORMAT_MAC = 30
            JID_FORMAT_MSP = 31
            JID_FORMAT_NCR = 32
            JID_FORMAT_PBM = 33
            JID_FORMAT_PCD = 34
            JID_FORMAT_PCX = 35
            JID_FORMAT_PDF = 36
            JID_FORMAT_PGM = 37
            JID_FORMAT_PIC = 38
            JID_FORMAT_PICT = 39
            JID_FORMAT_PNG = 40
            JID_FORMAT_PPM = 41
            JID_FORMAT_PSD = 42
            JID_FORMAT_PSP = 43
            JID_FORMAT_RAS = 44
            JID_FORMAT_RAW = 45
            JID_FORMAT_RGB = 46
            JID_FORMAT_RLE = 47
            JID_FORMAT_SCT = 48
            JID_FORMAT_SVG = 49
            JID_FORMAT_TGA = 50
            JID_FORMAT_TIF = 51
            JID_FORMAT_TXT = 52
            JID_FORMAT_WBMP = 53
            JID_FORMAT_WMF = 54
            JID_FORMAT_WPG = 55
            JID_FORMAT_XBM = 56
            JID_FORMAT_XPM = 57
            JID_FORMAT_XWD = 58
            JID_FORMAT_AS = 59
            JID_FORMAT_HDP = 60
            JID_FORMAT_MPO = 61
            JID_FORMAT_WEBP = 62
            JID_FORMAT_JPS = 63
            JID_FORMAT_PNS = 64
            JID_FORMAT_ANI = 100
            JID_FORMAT_AVI = 101
            JID_FORMAT_FLC = 102
            JID_FORMAT_FLI = 103
            JID_FORMAT_MID = 104
            JID_FORMAT_MNG = 105
            JID_FORMAT_MP3 = 106
            JID_FORMAT_MPG = 107
            JID_FORMAT_WAV = 108
            JID_FORMAT_CDR = 500
            JID_FORMAT_CMX = 501
            JID_FORMAT_DRW = 502
            JID_FORMAT_DXF = 503
            JID_FORMAT_GEM = 504
            JID_FORMAT_HGL = 505
            JID_FORMAT_VWPG = 506
            JID_MSI_START = 1000
            JID_MSI_END = 31999
            JID_FORMAT_GROUPS = 32000
            JID_FORMAT_MAXGROUPS = 32050
            JID_FORMAT_ALL = 32765
            JID_FORMAT_NONE = 32766
            def __init__(self):
                self.__name = "JascFileFormats"
                self.__desc = "File format codes "
                self.__values = [("JID_FORMAT_NOINFO", -1, "No info blank"),("JID_FORMAT_UNKNOWN", 0, "Format Unknown"),("JID_FORMAT_AFX", 1, "AFX file format"),("JID_FORMAT_BMP", 2, "BMP file format"),("JID_FORMAT_BRK", 3, "BRK file format"),("JID_FORMAT_CAL", 4, "CAL file format"),("JID_FORMAT_CGM", 5, "CGM file format"),("JID_FORMAT_CISRLE", 6, "CISRLE file format"),("JID_FORMAT_CLP", 7, "CLP file format"),("JID_FORMAT_CUR", 8, "CUR file format"),("JID_FORMAT_CUT", 9, "CUT file format"),("JID_FORMAT_DCX", 10, "DCX file format"),("JID_FORMAT_DGN", 11, "DGN file format"),("JID_FORMAT_DIB", 12, "DIB file format"),("JID_FORMAT_DWG", 13, "DWG file format"),("JID_FORMAT_EMF", 14, "EMF file format"),("JID_FORMAT_EPS", 15, "EPS file format"),("JID_FORMAT_FPX", 16, "FPX file format"),("JID_FORMAT_FSP", 17, "FSP file format"),("JID_FORMAT_GIF", 18, "GIF file format"),("JID_FORMAT_ICO", 19, "ICO file format"),("JID_FORMAT_IFF", 20, "IFF file format"),("JID_FORMAT_IMG", 21, "IMG file format"),("JID_FORMAT_JIF", 22, "JIF file format"),("JID_FORMAT_JP2", 23, "JP2 file format"),("JID_FORMAT_JPG", 24, "JPG file format"),("JID_FORMAT_KDC", 25, "KDC file format"),("JID_FORMAT_KFX", 26, "KFX file format"),("JID_FORMAT_LBM", 27, "LBM file format"),("JID_FORMAT_LPIC", 28, "LPIC file format"),("JID_FORMAT_LV", 29, "LV file format"),("JID_FORMAT_MAC", 30, "MAC file format"),("JID_FORMAT_MSP", 31, "MSP file format"),("JID_FORMAT_NCR", 32, "NCR file format"),("JID_FORMAT_PBM", 33, "PBM file format"),("JID_FORMAT_PCD", 34, "PCD file format"),("JID_FORMAT_PCX", 35, "PCX file format"),("JID_FORMAT_PDF", 36, "PDF file format"),("JID_FORMAT_PGM", 37, "PGM file format"),("JID_FORMAT_PIC", 38, "PIC file format"),("JID_FORMAT_PICT", 39, "PICT file format"),("JID_FORMAT_PNG", 40, "PNG file format"),("JID_FORMAT_PPM", 41, "PPM file format"),("JID_FORMAT_PSD", 42, "PSD file format"),("JID_FORMAT_PSP", 43, "PSP file format"),("JID_FORMAT_RAS", 44, "RAS file format"),("JID_FORMAT_RAW", 45, "RAW file format"),("JID_FORMAT_RGB", 46, "RGB file format"),("JID_FORMAT_RLE", 47, "RLE file format"),("JID_FORMAT_SCT", 48, "SCT file format"),("JID_FORMAT_SVG", 49, "SVG file format"),("JID_FORMAT_TGA", 50, "TGA file format"),("JID_FORMAT_TIF", 51, "TIF file format"),("JID_FORMAT_TXT", 52, "TXT file format"),("JID_FORMAT_WBMP", 53, "WBMP file format"),("JID_FORMAT_WMF", 54, "WMF file format"),("JID_FORMAT_WPG", 55, "WPG file format"),("JID_FORMAT_XBM", 56, "XBM file format"),("JID_FORMAT_XPM", 57, "XPM file format"),("JID_FORMAT_XWD", 58, "XWD file format"),("JID_FORMAT_AS", 59, "Animation Shop file format"),("JID_FORMAT_HDP", 60, "HDP file format"),("JID_FORMAT_MPO", 61, "Multiple Object file format"),("JID_FORMAT_WEBP", 62, "WebP file format"),("JID_FORMAT_JPS", 63, "Stereo Jpeg"),("JID_FORMAT_PNS", 64, "Stereo PNG"),("JID_FORMAT_ANI", 100, "ANI file format (base 100)"),("JID_FORMAT_AVI", 101, "AVI file format (base 100)"),("JID_FORMAT_FLC", 102, "FLC file format (base 100)"),("JID_FORMAT_FLI", 103, "FLI file format (base 100)"),("JID_FORMAT_MID", 104, "MID file format (base 100)"),("JID_FORMAT_MNG", 105, "MNG file format (base 100)"),("JID_FORMAT_MP3", 106, "MP3 file format (base 100)"),("JID_FORMAT_MPG", 107, "MPG file format (base 100)"),("JID_FORMAT_WAV", 108, "WAV file format (base 100)"),("JID_FORMAT_CDR", 500, "CDR file format (base 500)"),("JID_FORMAT_CMX", 501, "CMX file format (base 500)"),("JID_FORMAT_DRW", 502, "DRW file format (base 500)"),("JID_FORMAT_DXF", 503, "DXF file format (base 500)"),("JID_FORMAT_GEM", 504, "GEM file format (base 500)"),("JID_FORMAT_HGL", 505, "HGL file format (base 500)"),("JID_FORMAT_VWPG", 506, "VWPG file format (base 500)"),("JID_MSI_START", 1000, "MSI START file format (base 1000)"),("JID_MSI_END", 31999, "MSI END file format (base 1000)"),("JID_FORMAT_GROUPS", 32000, "FORMAT GROUPS (base 32000)"),("JID_FORMAT_MAXGROUPS", 32050, "FORMAT MAXGROUPS (base 32050)"),("JID_FORMAT_ALL", 32765, "JID_FORMAT_ALL  (base 32765)"),("JID_FORMAT_NONE", 32766, "JID_FORMAT_NONE (base 32766)"),]


        class __EventConst(PSPEnumType): 
            '''Describes events that have occurred that will force PSP to update caches or other internal structures.'''
            PictureTubeCache = 0
            PatternCache = 1
            TextureCache = 2
            GradientCache = 3
            BrushCache = 4
            PictureFrameCache = 5
            StyledLineCache = 6
            PluginCache = 7
            ScriptCache = 8
            PresetCache = 9
            SwatchesCache = 10
            MaskCache = 11
            SelectionCache = 12
            CMYKCache = 13
            PrintTemplateCache = 14
            WorkspaceCache = 15
            QuickGuideCache = 16
            PaletteCache = 17
            DeformationMapCache = 18
            EnvironmentMapCache = 19
            BumpMapCache = 20
            DisplacementMapCache = 21
            PresetShapeCache = 22
            FileOpenScriptCache = 23
            def __init__(self):
                self.__name = "Event"
                self.__desc = "Describes events that have occurred that will force PSP to update caches or other internal structures."
                self.__values = [("PictureTubeCache", 0, "Event has occured that invalidates the picture tube cache"),("PatternCache", 1, "Event has occured that invalidates the pattern cache"),("TextureCache", 2, "Event has occured that invalidates the texture cache"),("GradientCache", 3, "Event has occured that invalidates the gradient cache"),("BrushCache", 4, "Event has occured that invalidates the custom brush cache"),("PictureFrameCache", 5, "Event has occured that invalidates the picture frames cache"),("StyledLineCache", 6, "Event has occured that invalidates the styled lines cache"),("PluginCache", 7, "Event has occured that invalidates the plugin cache"),("ScriptCache", 8, "Event has occured that invalidates the script cache"),("PresetCache", 9, "Event has occured that invalidates the presets cache"),("SwatchesCache", 10, "Event has occured that invalidates the material swatches cache"),("MaskCache", 11, "Event has occured that invalidates the masks cache"),("SelectionCache", 12, "Event has occured that invalidates the selections cache"),("CMYKCache", 13, "Event has occured that invalidates the CMYK profiles cache"),("PrintTemplateCache", 14, "Event has occured that invalidates the print templates cache"),("WorkspaceCache", 15, "Event has occured that invalidates the workspaces cache"),("QuickGuideCache", 16, "Event has occured that invalidates the quick guides cache"),("PaletteCache", 17, "Event has occured that invalidates the palette cache"),("DeformationMapCache", 18, "Event has occured that invalidates the deformation map cache"),("EnvironmentMapCache", 19, "Event has occured that invalidates the environment map cache"),("BumpMapCache", 20, "Event has occured that invalidates the bump map cache"),("DisplacementMapCache", 21, "Event has occured that invalidates the displacement map cache"),("PresetShapeCache", 22, "Event has occured that invalidates the preset shapes cache"),("FileOpenScriptCache", 23, "Event has occured that invalidates the file open script cache"),]


        class __AutoShowPalettesConst(PSPEnumType): 
            '''Enables or disables automatic showing the palettes.'''
            Always = 0
            Never = 1
            WithLearningCenter = 2
            def __init__(self):
                self.__name = "AutoShowPalettes"
                self.__desc = "Enables or disables automatic showing the palettes."
                self.__values = [("Always", 0, "Always automatically show the palettes"),("Never", 1, "Never automatically show the palettes"),("WithLearningCenter", 2, "Automatically show the palettes if the Learning Center palette is open"),]


        class __BlackAndWhiteFilterColorConst(PSPEnumType): 
            '''Color of Lens Filter for Black And White Film Command'''
            Red = 0
            Yellow = 1
            Green = 2
            Blue = 3
            Orange = 4
            None = 5
            def __init__(self):
                self.__name = "BlackAndWhiteFilterColor"
                self.__desc = "Color of Lens Filter for Black And White Film Command"
                self.__values = [("Red", 0, "Red Lens Filter"),("Yellow", 1, "Yellow Lens Filter"),("Green", 2, "Green Lens Filter"),("Blue", 3, "Blue Lens Filter"),("Orange", 4, "Orange Lens Filter"),("None", 5, "No Lens Filter"),]


        class __CheckpointTransientDataConst(PSPEnumType): 
            '''Indicates what transient data to include in a checkpoint file/'''
            NoTransientData = 0
            NondiscardableTransientData = 1
            AllTransientData = 2
            def __init__(self):
                self.__name = "CheckpointTransientData"
                self.__desc = "Indicates what transient data to include in a checkpoint file/"
                self.__values = [("NoTransientData", 0, "Do not include any transient data."),("NondiscardableTransientData", 1, "Include nondiscardable transient data."),("AllTransientData", 2, "Include all transient data."),]


        class __GradientConst(PSPEnumType): 
            '''Defines the type of gradient; Linear, Radial, Rectangular, or Angular'''
            Linear = 0
            Sunburst = 1
            Rectangular = 2
            Radial = 3
            def __init__(self):
                self.__name = "Gradient"
                self.__desc = "Defines the type of gradient; Linear, Radial, Rectangular, or Angular"
                self.__values = [("Linear", 0, "Use linear algorithm to create the gradient."),("Sunburst", 1, "Use sunburst algorithm to create the gradient."),("Rectangular", 2, "Use rectangular algorithm to create the gradient."),("Radial", 3, "Use radial algorithm to create the gradient."),]


        class __PictureFrameTargetConst(PSPEnumType): 
            '''Defines whether the canvas or the current layer will have a Picture Frame applied to it.'''
            Canvas = 0
            CurrentLayer = 1
            def __init__(self):
                self.__name = "PictureFrameTarget"
                self.__desc = "Defines whether the canvas or the current layer will have a Picture Frame applied to it."
                self.__values = [("Canvas", 0, "Apply frame to canvas bounds."),("CurrentLayer", 1, "Apply frame to current layer bounds."),]


        class __CheckpointDataFormatConst(PSPEnumType): 
            '''The format of the checkpoint file.'''
            CRC = 0
            Text = 1
            Binary = 2
            def __init__(self):
                self.__name = "CheckpointDataFormat"
                self.__desc = "The format of the checkpoint file."
                self.__values = [("CRC", 0, "Checkpoint image data as a CRC value."),("Text", 1, "Checkpoint image data as a hexadecimal text."),("Binary", 2, "Checkpoint image data as a binary data."),]


        class __SharpenModeConst(PSPEnumType): 
            '''Sharpen mode for raw camera data'''
            Low = 0
            Normal = 1
            High = 2
            Standard = 3
            Off = 4
            def __init__(self):
                self.__name = "SharpenMode"
                self.__desc = "Sharpen mode for raw camera data"
                self.__values = [("Low", 0, "Low"),("Normal", 1, "Normal"),("High", 2, "High"),("Standard", 3, "Standard"),("Off", 4, "Off"),]


        class __WhiteBalanceConst(PSPEnumType): 
            '''White balance modes for raw camera data'''
            AsShot = 0
            Incandescent = 1
            Flourscent = 2
            Sunny = 3
            Cloudy = 4
            Shade = 5
            Flash = 6
            def __init__(self):
                self.__name = "WhiteBalance"
                self.__desc = "White balance modes for raw camera data"
                self.__values = [("AsShot", 0, "As shot"),("Incandescent", 1, "Incandescent"),("Flourscent", 2, "Flourscent"),("Sunny", 3, "Sunny"),("Cloudy", 4, "Cloudy"),("Shade", 5, "Shade"),("Flash", 6, "Flash"),]


        class __MouseButtonConst(PSPEnumType): 
            '''AN indication of the mouse button used in an operation.'''
            Primary = 0
            Secondary = 1
            def __init__(self):
                self.__name = "MouseButton"
                self.__desc = "AN indication of the mouse button used in an operation."
                self.__values = [("Primary", 0, "The primary button was used."),("Secondary", 1, "The secondary button was used."),]


        class __ImageInfoPropertySheetConst(PSPEnumType): 
            '''Active Page of Image Information Dialog'''
            ImagePage = 0
            CreatorPage = 1
            WatermarkPage = 2
            EXIFPage = 3
            def __init__(self):
                self.__name = "ImageInfoPropertySheet"
                self.__desc = "Active Page of Image Information Dialog"
                self.__values = [("ImagePage", 0, "Image Page"),("CreatorPage", 1, "Creator Page"),("WatermarkPage", 2, "Watermark Page"),("EXIFPage", 3, "EXIF Page"),]


        class __MixerSampleModeConst(PSPEnumType): 
            '''Sample mode for the mixer palette'''
            SampleMode1x1 = 0
            SampleMode3x3 = 1
            SampleMode5x5 = 2
            SampleMode7x7 = 3
            SampleMode9x9 = 4
            SampleMode11x11 = 5
            def __init__(self):
                self.__name = "MixerSampleMode"
                self.__desc = "Sample mode for the mixer palette"
                self.__values = [("SampleMode1x1", 0, "Samples 1x1 pixels"),("SampleMode3x3", 1, "Samples 3x3 pixels"),("SampleMode5x5", 2, "Samples 5x5 pixels"),("SampleMode7x7", 3, "Samples 7x7 pixels"),("SampleMode9x9", 4, "Samples 9x9 pixels"),("SampleMode11x11", 5, "Samples 11x11 pixels"),]


        class __MixerActiveToolConst(PSPEnumType): 
            '''Active tool of the mixer palette'''
            Knife = 0
            Tube = 1
            Dropper = 2
            def __init__(self):
                self.__name = "MixerActiveTool"
                self.__desc = "Active tool of the mixer palette"
                self.__values = [("Knife", 0, "Knife is active"),("Tube", 1, "Tube is active"),("Dropper", 2, "Dropper is active"),]


        class __MixerModeConst(PSPEnumType): 
            '''Preparing or Sampling'''
            Prepare = 0
            Sample = 1
            def __init__(self):
                self.__name = "MixerMode"
                self.__desc = "Preparing or Sampling"
                self.__values = [("Prepare", 0, "Preparing the mix area"),("Sample", 1, "Sampling from the mix area"),]


        class __ResourceListViewConst(PSPEnumType): 
            '''ResourceListView'''
            Text = 0
            LargeThumbnails = 1
            SmallThumbnails = 2
            def __init__(self):
                self.__name = "ResourceListView"
                self.__desc = "ResourceListView"
                self.__values = [("Text", 0, ""),("LargeThumbnails", 1, ""),("SmallThumbnails", 2, ""),]


        class __ArtMediaPencilStyleConst(PSPEnumType): 
            '''Specifies the pencil surfaced used for drawing.'''
            Tilt = 0
            Tip = 1
            Edge = 2
            def __init__(self):
                self.__name = "ArtMediaPencilStyle"
                self.__desc = "Specifies the pencil surfaced used for drawing."
                self.__values = [("Tilt", 0, "Select between tip style and edge style based upon stylus tilt."),("Tip", 1, "Treat the pencil as if the tip were being used for drawing."),("Edge", 2, "Treat the pencil as if the edge were being used for drawing."),]


        class __ArtMediaBrushCleaningConst(PSPEnumType): 
            '''Specifies how the brush head is cleansed of picked up color after a stroke.'''
            AutomaticClean = 0
            ManualClean = 1
            def __init__(self):
                self.__name = "ArtMediaBrushCleaning"
                self.__desc = "Specifies how the brush head is cleansed of picked up color after a stroke."
                self.__values = [("AutomaticClean", 0, "The brush is autoatically cleaned of all media after the stroke."),("ManualClean", 1, "The brush retains any media from the last stroke until manually cleaned."),]


        class __ArtMediaBrushShapeConst(PSPEnumType): 
            '''The shape of the brush head.'''
            Elliptical = 0
            Rectangular = 1
            def __init__(self):
                self.__name = "ArtMediaBrushShape"
                self.__desc = "The shape of the brush head."
                self.__values = [("Elliptical", 0, "An elliptical brush head."),("Rectangular", 1, "A rectangular brush head."),]


        class __ArtMediaBrushRotationConst(PSPEnumType): 
            '''Specifies whether the brush head maintains a fixed angle or rotates along the stroke path.'''
            FixedAngle = 0
            RotateAlongPath = 1
            def __init__(self):
                self.__name = "ArtMediaBrushRotation"
                self.__desc = "Specifies whether the brush head maintains a fixed angle or rotates along the stroke path."
                self.__values = [("FixedAngle", 0, "Brush head maintains a fixed angle."),("RotateAlongPath", 1, "Brush head rotates along stroke path."),]


        class __AntialiasExConst(PSPEnumType): 
            '''Text antialias value which defines mode to use.'''
            None = 0
            Sharp = 1
            Smooth = 2
            def __init__(self):
                self.__name = "AntialiasEx"
                self.__desc = "Text antialias value which defines mode to use."
                self.__values = [("None", 0, "No anitaliasing."),("Sharp", 1, "Use Sharp antialiasing."),("Smooth", 2, "Use Smooth antialiasing."),]


        class __NewLayerTypeConst(PSPEnumType): 
            '''New layer type'''
            ArtMedia = 0
            Raster = 1
            Vector = 2
            def __init__(self):
                self.__name = "NewLayerType"
                self.__desc = "New layer type"
                self.__values = [("ArtMedia", 0, "Art Media Layer"),("Raster", 1, "Raster Layer"),("Vector", 2, "Vector Layer"),]


        class __TextFlowConst(PSPEnumType): 
            '''Defines text line and character direction.'''
            HorizontalDown = 0
            VerticalLeft = 1
            VerticalRight = 2
            HorizontalUp = 3
            def __init__(self):
                self.__name = "TextFlow"
                self.__desc = "Defines text line and character direction."
                self.__values = [("HorizontalDown", 0, "Characters flow horizontally and lines flow down."),("VerticalLeft", 1, "Characters flow vertically and lines flow left."),("VerticalRight", 2, "Characters flow vertically and lines flow right."),("HorizontalUp", 3, ""),]


        class __InitializeToConst(PSPEnumType): 
            '''Controls how the parameters of a command are initialized.'''
            Default = 0
            Random = 1
            LastUsed = 2
            CurrentTool = 3
            def __init__(self):
                self.__name = "InitializeTo"
                self.__desc = "Controls how the parameters of a command are initialized."
                self.__values = [("Default", 0, "Starts with factory default values"),("Random", 1, "Starts with randomized values"),("LastUsed", 2, "Starts with the last used values"),("CurrentTool", 3, "For tool commands, starts with the settings currently on the tool options palette"),]


        class __PathEntryTypeConst(PSPEnumType): 
            '''Describes the type of point in a path parameter'''
            MoveTo = 0
            LineTo = 1
            CurveTo = 2
            Closepath = 3
            MoveToEx = 4
            CurveToEx = 5
            def __init__(self):
                self.__name = "PathEntryType"
                self.__desc = "Describes the type of point in a path parameter"
                self.__values = [("MoveTo", 0, "Point is a move to - moves to the point without drawing"),("LineTo", 1, "Point is a line to - draws a straight line from the previous point"),("CurveTo", 2, "Point is a curve to - draws a bezier curve from the previous point to the end point, using 2 control handles"),("Closepath", 3, "Close the path - draw back to the beginning point"),("MoveToEx", 4, "Point is a move to - moves to a point without drawing"),("CurveToEx", 5, "Point is a curve to - draws a bezier curve from the previous point to the end point, using 2 control handles"),]


        class __NoiseTypeConst(PSPEnumType): 
            '''Type of noise'''
            Random = 0
            Uniform = 1
            Gaussian = 2
            def __init__(self):
                self.__name = "NoiseType"
                self.__desc = "Type of noise"
                self.__values = [("Random", 0, "Random noise"),("Uniform", 1, "Uniform noise"),("Gaussian", 2, "Gaussian noise"),]


        class __PointRelativeBasisConst(PSPEnumType): 
            '''PointRelativeBasis'''
            Canvas = 0
            Layer = 1
            Document = 2
            def __init__(self):
                self.__name = "PointRelativeBasis"
                self.__desc = "PointRelativeBasis"
                self.__values = [("Canvas", 0, ""),("Layer", 1, ""),("Document", 2, ""),]


        class __BatchModeConst(PSPEnumType): 
            '''The save mode for batch processing.'''
            NewType = 0
            Copy = 1
            Overwrite = 2
            ObeyScript = 3
            def __init__(self):
                self.__name = "BatchMode"
                self.__desc = "The save mode for batch processing."
                self.__values = [("NewType", 0, "Save the file to a new file after processing."),("Copy", 1, "Run the script and save to a copy of the original type"),("Overwrite", 2, "Run a script and then save to the original file"),("ObeyScript", 3, "Only execute the script do not save"),]


        class __PaletteTransparencyConst(PSPEnumType): 
            '''Type of palette transparency.'''
            NoTransparency = 0
            BackgroundColor = 1
            PaletteEntry = 2
            def __init__(self):
                self.__name = "PaletteTransparency"
                self.__desc = "Type of palette transparency."
                self.__values = [("NoTransparency", 0, "No color is transparent."),("BackgroundColor", 1, "Make background color transparent."),("PaletteEntry", 2, "Make specified palette entry transparent."),]


        class __PaletteMethodConst(PSPEnumType): 
            '''Palette or palette generation method to use.'''
            OptimizedMedianCut = 0
            OptimizedOctree = 1
            Windows = 2
            StandardWebSafe = 3
            def __init__(self):
                self.__name = "PaletteMethod"
                self.__desc = "Palette or palette generation method to use."
                self.__values = [("OptimizedMedianCut", 0, "Optimized median cut method."),("OptimizedOctree", 1, "Optimized octree method."),("Windows", 2, "Windows method."),("StandardWebSafe", 3, "Standard/web safe method."),]


        class __ErrorDiffusionConst(PSPEnumType): 
            '''Error diffusion color reduction method subtypes.'''
            FloydSteinberg = 0
            Burkes = 1
            Stucki = 2
            def __init__(self):
                self.__name = "ErrorDiffusion"
                self.__desc = "Error diffusion color reduction method subtypes."
                self.__values = [("FloydSteinberg", 0, "Floyd-Steinberg type."),("Burkes", 1, "Burkes type."),("Stucki", 2, "Stucki type."),]


        class __PaletteComponentConst(PSPEnumType): 
            '''Palette component: grey, red, green, blue.'''
            GreyValues = 0
            RedComponent = 1
            GreenComponent = 2
            BlueComponent = 3
            def __init__(self):
                self.__name = "PaletteComponent"
                self.__desc = "Palette component: grey, red, green, blue."
                self.__values = [("GreyValues", 0, "Grey values"),("RedComponent", 1, "Red component"),("GreenComponent", 2, "Green component"),("BlueComponent", 3, "Blue component"),]


        class __ReductionMethodConst(PSPEnumType): 
            '''The method used to replace a palette.'''
            NearestColorMatch = 0
            OrderedDither = 1
            ErrorDiffusionDither = 2
            MaintainIndexes = 3
            def __init__(self):
                self.__name = "ReductionMethod"
                self.__desc = "The method used to replace a palette."
                self.__values = [("NearestColorMatch", 0, "Finds nearest colors."),("OrderedDither", 1, "Ordered dither."),("ErrorDiffusionDither", 2, "Dithers colors."),("MaintainIndexes", 3, "Loads palette in place of the other without changing the image bitmap."),]


        class __TonalRangeConst(PSPEnumType): 
            '''Tonal ranges.'''
            None = 0
            Shadow = 1
            Midtones = 2
            Highlights = 3
            def __init__(self):
                self.__name = "TonalRange"
                self.__desc = "Tonal ranges."
                self.__values = [("None", 0, "None"),("Shadow", 1, "Lower range"),("Midtones", 2, "Middle range"),("Highlights", 3, "Upper range"),]


        class __TransformTypeConst(PSPEnumType): 
            '''Determines which type of transform will occur when the transform apply button is pressed in the Pen tool options bar.'''
            DuplicateAndOffset = 0
            Rotate = 1
            SkewX = 2
            SkewY = 3
            Expand = 4
            Contract = 5
            def __init__(self):
                self.__name = "TransformType"
                self.__desc = "Determines which type of transform will occur when the transform apply button is pressed in the Pen tool options bar."
                self.__values = [("DuplicateAndOffset", 0, "Duplicates and offsets the currently selected nodes"),("Rotate", 1, "Rotates the currently selected nodes"),("SkewX", 2, "Horizontally skews the currently selected nodes"),("SkewY", 3, "Vertically skews the currently selected nodes"),("Expand", 4, "Expands the currently selected nodes"),("Contract", 5, "Contracts the currently selected nodes"),]


        class __LensMapTypeConst(PSPEnumType): 
            '''Type of the map that can be used for Magnifying Lens effect'''
            CurrentImage = 0
            Environment = 1
            def __init__(self):
                self.__name = "LensMapType"
                self.__desc = "Type of the map that can be used for Magnifying Lens effect"
                self.__values = [("CurrentImage", 0, "Current Image"),("Environment", 1, "Environment"),]


        class __DimensionTypeConst(PSPEnumType): 
            '''Dimension type of new file'''
            Pixels = 0
            Inches = 1
            Centimeters = 2
            Millimeters = 3
            def __init__(self):
                self.__name = "DimensionType"
                self.__desc = "Dimension type of new file"
                self.__values = [("Pixels", 0, "Pixels"),("Inches", 1, "Inches"),("Centimeters", 2, "Centimeters"),("Millimeters", 3, "Millimeters"),]


        class __ColordepthConst(PSPEnumType): 
            '''Color depth for a new image'''
            BlackAndWhite = 0
            SixteenColors = 1
            Greyscale = 2
            TwoFiftySixColor = 3
            SixteenMillionColor = 4
            SixteenBitGreyscale = 5
            SixteenBitColor = 6
            def __init__(self):
                self.__name = "Colordepth"
                self.__desc = "Color depth for a new image"
                self.__values = [("BlackAndWhite", 0, "Black and White Image (1 bit)"),("SixteenColors", 1, "16 colors Image (4 bit)"),("Greyscale", 2, "Greyscale Image (8 bit)"),("TwoFiftySixColor", 3, "256 Color Image (8 bit)"),("SixteenMillionColor", 4, "16 Million Color Image (24 bit)"),("SixteenBitGreyscale", 5, "Greyscale Image (16 bit)"),("SixteenBitColor", 6, "256 Trillion Color Image (48 bit)"),]


        class __ColorCorrectionConst(PSPEnumType): 
            '''Describes the manual color correction method'''
            Preset = 0
            Manual = 1
            def __init__(self):
                self.__name = "ColorCorrection"
                self.__desc = "Describes the manual color correction method"
                self.__values = [("Preset", 0, "Match to a preset color"),("Manual", 1, "Match to a user defined color"),]


        class __ParamInfoConst(PSPEnumType): 
            '''Controls what parameter information is returned from GetCommandInfo. '''
            None = 0
            Default = 1
            LastUsed = 2
            def __init__(self):
                self.__name = "ParamInfo"
                self.__desc = "Controls what parameter information is returned from GetCommandInfo. "
                self.__values = [("None", 0, "No parameter information is returned"),("Default", 1, "Factory default parameter information is returned"),("LastUsed", 2, "Last used parameter values are returned"),]


        class __PaletteFormatConst(PSPEnumType): 
            '''Specifies either PSP or Microsoft color palette format.'''
            PSPPaletteFormat = 0
            MicrosoftPaletteFormat = 1
            JascPaletteFormat = 2
            def __init__(self):
                self.__name = "PaletteFormat"
                self.__desc = "Specifies either PSP or Microsoft color palette format."
                self.__values = [("PSPPaletteFormat", 0, "*.PspPalette (PSP) format"),("MicrosoftPaletteFormat", 1, "*.pal (Microsoft) format"),("JascPaletteFormat", 2, "*.PspPalette (PSP) format"),]


        class __MatchModeConst(PSPEnumType): 
            '''Specifies match modes'''
            None = 0
            RGBValue = 1
            AllOpaque = 4
            Opacity = 5
            Hue = 6
            Traditional = 7
            Perceptual = 8
            Brightness = 9
            Color = 10
            def __init__(self):
                self.__name = "MatchMode"
                self.__desc = "Specifies match modes"
                self.__values = [("None", 0, "None"),("RGBValue", 1, "RGB Value"),("AllOpaque", 4, "All Opaque"),("Opacity", 5, "Opacity"),("Hue", 6, "Hue"),("Traditional", 7, "Traditional"),("Perceptual", 8, "Perceptual"),("Brightness", 9, "Brightness"),("Color", 10, "Color"),]


        class __HistogramEditModeConst(PSPEnumType): 
            '''Specifies if luminance or color channels should be modified'''
            Luminance = 0
            Color = 1
            def __init__(self):
                self.__name = "HistogramEditMode"
                self.__desc = "Specifies if luminance or color channels should be modified"
                self.__values = [("Luminance", 0, "Edit luminance"),("Color", 1, "Edit color channels"),]


        class __GridColorSchemeConst(PSPEnumType): 
            '''Defined color scheme for transparency grid.'''
            SolidWhite = 0
            SolidRed = 1
            SolidGreen = 2
            SolidBlue = 3
            SolidBlack = 4
            SolidGrey = 5
            SolidYellow = 6
            SolidCyan = 7
            SolidPink = 8
            LightGrey = 9
            MediumGrey = 10
            DarkGrey = 11
            Red = 12
            Green = 13
            Blue = 14
            Custom1 = 15
            Custom2 = 16
            Custom3 = 17
            Custom4 = 18
            Custom5 = 19
            Custom6 = 20
            Custom7 = 21
            Custom8 = 22
            Custom9 = 23
            def __init__(self):
                self.__name = "GridColorScheme"
                self.__desc = "Defined color scheme for transparency grid."
                self.__values = [("SolidWhite", 0, "solid white"),("SolidRed", 1, "solid red"),("SolidGreen", 2, "solid green"),("SolidBlue", 3, "solid blue"),("SolidBlack", 4, "solid black"),("SolidGrey", 5, "solid grey"),("SolidYellow", 6, "solid yellow"),("SolidCyan", 7, "solid cyan"),("SolidPink", 8, "solid pink"),("LightGrey", 9, "light grey"),("MediumGrey", 10, "medium grey"),("DarkGrey", 11, "dark grey"),("Red", 12, "red"),("Green", 13, "green"),("Blue", 14, "blue"),("Custom1", 15, "custom 1"),("Custom2", 16, "custom 2"),("Custom3", 17, "custom 3"),("Custom4", 18, "custom 4"),("Custom5", 19, "custom 5"),("Custom6", 20, "custom 6"),("Custom7", 21, "custom 7"),("Custom8", 22, "custom 8"),("Custom9", 23, "custom 9"),]


        class __AppOutputFilteringConst(PSPEnumType): 
            '''Defines the amount of output the application sends to the script output window.  Each level includes all of the data from the previous level.'''
            None = 0
            ErrorOnly = 1
            Minimal = 2
            Normal = 3
            Verbose = 4
            Timing = 5
            def __init__(self):
                self.__name = "AppOutputFiltering"
                self.__desc = "Defines the amount of output the application sends to the script output window.  Each level includes all of the data from the previous level."
                self.__values = [("None", 0, "All application output suppressed."),("ErrorOnly", 1, "All output except error messages suppressed."),("Minimal", 2, "Internal use only."),("Normal", 3, "Command logging done for all commands executed silently."),("Verbose", 4, "Library load tracing is displayed"),("Timing", 5, "Library load and command execution timing data displayed."),]


        class __SelectionTypeConst(PSPEnumType): 
            '''Describes the type of raster selection that exists - none, floating, or non-floating'''
            None = 0
            Floating = 1
            NonFloating = 2
            def __init__(self):
                self.__name = "SelectionType"
                self.__desc = "Describes the type of raster selection that exists - none, floating, or non-floating"
                self.__values = [("None", 0, "No selection exists"),("Floating", 1, "A floating selection exists"),("NonFloating", 2, "A non-floating selection exists"),]


        class __MapShapeTypeConst(PSPEnumType): 
            '''Type of map shape'''
            Undefined = 0
            Polygon = 1
            Rectangle = 2
            Circle = 3
            def __init__(self):
                self.__name = "MapShapeType"
                self.__desc = "Type of map shape"
                self.__values = [("Undefined", 0, "Type not defined"),("Polygon", 1, "Shape is a polygon"),("Rectangle", 2, "Shape is a rectangle"),("Circle", 3, "Shape is a circle"),]


        class __WebFileTypeConst(PSPEnumType): 
            '''Web file format'''
            Gif = 0
            Jpeg = 1
            Png = 2
            def __init__(self):
                self.__name = "WebFileType"
                self.__desc = "Web file format"
                self.__values = [("Gif", 0, "Gif file"),("Jpeg", 1, "Jpeg file"),("Png", 2, "Png file"),]


        class __WebFrameTargetConst(PSPEnumType): 
            '''Target frame or window in which the image is to open'''
            Blank = 0
            Parent = 1
            Self = 2
            Top = 3
            UseDefault = 4
            def __init__(self):
                self.__name = "WebFrameTarget"
                self.__desc = "Target frame or window in which the image is to open"
                self.__values = [("Blank", 0, "Loads image in new browser"),("Parent", 1, "Loads image in parent window"),("Self", 2, "Loads image in same window"),("Top", 3, "Loads image in full window"),("UseDefault", 4, "Use the default"),]


        class __AutoActionModeConst(PSPEnumType): 
            '''Controls behavior of auto actions when command is run'''
            Match = 0
            AllNever = 1
            DemoteAsk = 2
            Default = 3
            PromoteAsk = 4
            AllAlways = 5
            def __init__(self):
                self.__name = "AutoActionMode"
                self.__desc = "Controls behavior of auto actions when command is run"
                self.__values = [("Match", 0, "Set auto action mode according to execution mode (if interactive, use Normal, for silent use PromoteAsk)"),("AllNever", 1, "Do not execute any auto actions"),("DemoteAsk", 2, "Convert all auto actions marked as Ask to Never"),("Default", 3, "Do auto actions as specified by preferences"),("PromoteAsk", 4, "Convert all auto actions marked as Ask to Always"),("AllAlways", 5, "Execute all auto actions without prompting"),]


        class __FileFormatConst(PSPEnumType): 
            '''File Format Type'''
            Unknown = 0
            AFX = 1
            BMP = 2
            BRK = 3
            CAL = 4
            CDR = 5
            CGM = 6
            CLP = 7
            CMX = 8
            CUR = 9
            CUT = 10
            DCX = 11
            DGN = 12
            DIB = 13
            DRW = 14
            DWG = 15
            DXF = 16
            EMF = 17
            EPS = 18
            FPX = 19
            GEM = 20
            GIF = 21
            HGL = 22
            IFF = 23
            IMG = 24
            JP2 = 25
            JPG = 26
            KDC = 27
            KFX = 28
            LBM = 29
            LPIC = 30
            LV = 31
            MAC = 32
            MSP = 33
            NCR = 34
            PBM = 35
            PCD = 36
            PCX = 37
            PDF = 38
            PGM = 39
            PIC = 40
            PICT = 41
            PNG = 42
            PPM = 43
            PSD = 44
            FSP = 45
            PSP = 46
            RAS = 47
            RAW = 48
            RGB = 49
            RLE = 50
            SCT = 51
            SVG = 52
            TGA = 53
            TIF = 54
            VWPG = 55
            WBMP = 56
            WMF = 57
            WPG = 58
            XBM = 59
            XPM = 60
            XWD = 61
            AS = 62
            Plugin = 63
            CAMERARAW = 64
            RIFF = 65
            HDP = 66
            MPO = 67
            UFO = 68
            WEBP = 69
            JPS = 70
            PNS = 71
            def __init__(self):
                self.__name = "FileFormat"
                self.__desc = "File Format Type"
                self.__values = [("Unknown", 0, "Unknown file format type"),("AFX", 1, "AutoFX"),("BMP", 2, "Windows or OS/2 Bitmap"),("BRK", 3, "Brooktrout Fax"),("CAL", 4, "CALS Raster"),("CDR", 5, "CorelDraw Drawing"),("CGM", 6, "Computer Graphics Metafile"),("CLP", 7, "Windows Clipboard"),("CMX", 8, "Corel Clipart"),("CUR", 9, "Windows Cursor"),("CUT", 10, "Dr. Halo"),("DCX", 11, "Zsoft Multipage Paintbrush"),("DGN", 12, "MicroStation Drawing"),("DIB", 13, "Windows or OS/2 DIB"),("DRW", 14, "Micrografx Draw"),("DWG", 15, "AutoCAD Drawing"),("DXF", 16, "Autodesk Drawing Interchange"),("EMF", 17, "Windows Enhanced Meta File"),("EPS", 18, "Encapsulated PostScript"),("FPX", 19, "FlashPix"),("GEM", 20, "Ventura/GEM Drawing"),("GIF", 21, "CompuServe Graphics Interchange"),("HGL", 22, "HP Graphics Language"),("IFF", 23, "Amiga Interchange"),("IMG", 24, "GEM Paint"),("JP2", 25, "JPEG 2000"),("JPG", 26, "JPEG - JFIF Compliant"),("KDC", 27, "Kodak Digital Camera File"),("KFX", 28, "Kofax"),("LBM", 29, "Deluxe Paint"),("LPIC", 30, "Lotus PIC"),("LV", 31, "Lazer View"),("MAC", 32, "MacPaint"),("MSP", 33, "Microsoft Paint"),("NCR", 34, "NCR G4"),("PBM", 35, "Portable Bitmap"),("PCD", 36, "Kodak Photo CD"),("PCX", 37, "Zsoft Paintbrush"),("PDF", 38, "Portable Document File"),("PGM", 39, "Portable Greymap"),("PIC", 40, "PC Paint"),("PICT", 41, "Macintosh PICT"),("PNG", 42, "Portable Network Graphics"),("PPM", 43, "Portable Pixelmap"),("PSD", 44, "Photoshop"),("FSP", 45, "FastPict"),("PSP", 46, "PaintShop Pro Image"),("RAS", 47, "Sun Raster Image"),("RAW", 48, "RAW (graphics) File Format"),("RGB", 49, "SGI Image File"),("RLE", 50, "Windows or CompuServe RLE"),("SCT", 51, "SciTex Continuous Tone"),("SVG", 52, "Scalable Vector Graphics"),("TGA", 53, "Truevision Targa"),("TIF", 54, "Tagged Image File Format"),("VWPG", 55, "WordPerfect Vector"),("WBMP", 56, "Wireless Bitmap"),("WMF", 57, "Windows Meta File"),("WPG", 58, "WordPerfect Bitmap"),("XBM", 59, "X Windows Bitmap"),("XPM", 60, "X Windows Pixmap"),("XWD", 61, "X Windows Dump"),("AS", 62, "Animation Shop Image"),("Plugin", 63, "Plugin file format type"),("CAMERARAW", 64, "Raw Camera Data"),("RIFF", 65, "Painter Document"),("HDP", 66, "HD Photo"),("MPO", 67, "Multiple Picture Object"),("UFO", 68, "Ulead File Object"),("WEBP", 69, "WebP"),("JPS", 70, "Stereo JPG"),("PNS", 71, "Stereo PNG"),]


        class __ObjectPlacementConst(PSPEnumType): 
            '''This is the placement enumeration for the movement of vector objects in the layers palette.'''
            SiblingNone = 0
            SiblingAbove = 1
            SiblingBelow = 2
            def __init__(self):
                self.__name = "ObjectPlacement"
                self.__desc = "This is the placement enumeration for the movement of vector objects in the layers palette."
                self.__values = [("SiblingNone", 0, "The objects are not being placed in relation to a sibling.  The parent is where the objects are attached."),("SiblingAbove", 1, "Attach the objects to the sibling above the current drop position."),("SiblingBelow", 2, "Attach the objects to the sibling below the drop point"),]


        class __MeshWarpingSymmetricModeConst(PSPEnumType): 
            '''Mesh symmetric mode'''
            NonSymmetric = 0
            SymmetricHLeads = 1
            SymmetricVLeads = 2
            def __init__(self):
                self.__name = "MeshWarpingSymmetricMode"
                self.__desc = "Mesh symmetric mode"
                self.__values = [("NonSymmetric", 0, "Non symmetric mesh"),("SymmetricHLeads", 1, "Symmetric mesh horizontal size leads"),("SymmetricVLeads", 2, "Symmetric mesh vertical size leads"),]


        class __GeneralPreferencesTabsConst(PSPEnumType): 
            '''Ordinal for the general preferences tabs; in display order.'''
            Undo = 0
            View = 1
            Display = 2
            WindowsAndPalettes = 3
            Browser = 4
            Miscellaneous = 5
            Units = 6
            Transparency = 7
            PhotoSharing = 8
            Warnings = 9
            AutoAction = 10
            Multimedia = 11
            Organizer = 12
            AutoPreserve = 13
            def __init__(self):
                self.__name = "GeneralPreferencesTabs"
                self.__desc = "Ordinal for the general preferences tabs; in display order."
                self.__values = [("Undo", 0, "Undo tab"),("View", 1, "View tab"),("Display", 2, "Display tab"),("WindowsAndPalettes", 3, "Windows And Palettes tab"),("Browser", 4, "Browser tab"),("Miscellaneous", 5, "Miscellaneous tab"),("Units", 6, "Units tab"),("Transparency", 7, "Transparency tab"),("PhotoSharing", 8, "PhotoSharing tab"),("Warnings", 9, "Warnings tab"),("AutoAction", 10, "Auto Action tab"),("Multimedia", 11, "Multimedia tab"),("Organizer", 12, "Manage tab"),("AutoPreserve", 13, "Auto-Preserve tab"),]


        class __CropUnitsConst(PSPEnumType): 
            '''Crop by pixels, inches, or centimeters'''
            Pixels = 0
            Inches = 1
            Centimeters = 2
            def __init__(self):
                self.__name = "CropUnits"
                self.__desc = "Crop by pixels, inches, or centimeters"
                self.__values = [("Pixels", 0, "Crop by pixels"),("Inches", 1, "Crop by inches"),("Centimeters", 2, "Crop by Centimeters"),]


        class __CropModeConst(PSPEnumType): 
            '''Mode for crop tool'''
            ClearRect = 0
            Custom = 1
            CustomAR = 2
            CustomPrint = 3
            CropSelection = 4
            OpaqueLayer = 5
            OpaqueMerged = 6
            def __init__(self):
                self.__name = "CropMode"
                self.__desc = "Mode for crop tool"
                self.__values = [("ClearRect", 0, "Clear rect shown"),("Custom", 1, "User selected crop area"),("CustomAR", 2, "User selected crop area - Maintain Aspect Ratio"),("CustomPrint", 3, "User selected crop area - Update Print size"),("CropSelection", 4, "Crop to selection"),("OpaqueLayer", 5, "Crop to Opaque area on current layer"),("OpaqueMerged", 6, "Crop to Opaque area on Merged image"),]


        class __TubeSelectionModeConst(PSPEnumType): 
            '''Tube selection mode'''
            Random = 0
            Incremental = 1
            Angular = 2
            Pressure = 3
            Velocity = 4
            def __init__(self):
                self.__name = "TubeSelectionMode"
                self.__desc = "Tube selection mode"
                self.__values = [("Random", 0, "Next image selection is random"),("Incremental", 1, "Next image selection is next in the series."),("Angular", 2, "Next image selection follows same direction as cursor on main image"),("Pressure", 3, "Next image selection is determined by the pressure pad"),("Velocity", 4, "Next image selection is determined by the speed of the cursor movement"),]


        class __TubePlacementModeConst(PSPEnumType): 
            '''Placement mode of the tube'''
            Random = 0
            Continuous = 1
            def __init__(self):
                self.__name = "TubePlacementMode"
                self.__desc = "Placement mode of the tube"
                self.__values = [("Random", 0, "Random placement"),("Continuous", 1, "Continuous placement"),]


        class __WarpingBrushFinalApplyQualityConst(PSPEnumType): 
            '''Warping brush Final Apply quality.'''
            Omit = 0
            Use = 1
            def __init__(self):
                self.__name = "WarpingBrushFinalApplyQuality"
                self.__desc = "Warping brush Final Apply quality."
                self.__values = [("Omit", 0, "Don't use final apply quality enhacement."),("Use", 1, "Finest final apply quality."),]


        class __WarpingBrushDraftQualityConst(PSPEnumType): 
            '''Warping brush draft quality.'''
            High = 0
            Medium = 2
            Low = 3
            Coarse = 4
            def __init__(self):
                self.__name = "WarpingBrushDraftQuality"
                self.__desc = "Warping brush draft quality."
                self.__values = [("High", 0, "High quality"),("Medium", 2, "Medium quality"),("Low", 3, "Low quality"),("Coarse", 4, "Coarse quality"),]


        class __WarpingBrushEdgeModeConst(PSPEnumType): 
            '''Warping brush edge mode.'''
            Background = 0
            Fixed = 1
            Wraparound = 2
            def __init__(self):
                self.__name = "WarpingBrushEdgeMode"
                self.__desc = "Warping brush edge mode."
                self.__values = [("Background", 0, "Background or transparency fill."),("Fixed", 1, "Fixed."),("Wraparound", 2, "Wraparound."),]


        class __LayerTypeConst(PSPEnumType): 
            '''Defines the type of a layer'''
            Raster = 0
            Vector = 1
            Group = 2
            Mask = 3
            ColorBalance = 4
            ChannelMixer = 5
            Curves = 6
            HueSatLum = 7
            Posterize = 8
            Threshold = 9
            Invert = 10
            Levels = 11
            BrightnessContrast = 12
            Selection = 13
            FloatingSelection = 14
            ArtMedia = 15
            Vibrancy = 16
            Histogram = 17
            LocalToneMapping = 18
            FillLightClarity = 19
            SmartFix = 20
            def __init__(self):
                self.__name = "LayerType"
                self.__desc = "Defines the type of a layer"
                self.__values = [("Raster", 0, "Raster layer"),("Vector", 1, "Vector layer"),("Group", 2, "Group layer"),("Mask", 3, "Mask layer"),("ColorBalance", 4, "White balance adjustment layer"),("ChannelMixer", 5, "Channel mixer adjustment layer"),("Curves", 6, "Curves adjustment layer"),("HueSatLum", 7, "HSL adjustment layer"),("Posterize", 8, "Posterize adjustment layer"),("Threshold", 9, "Threshold adjustment layer"),("Invert", 10, "Invert adjustment layer"),("Levels", 11, "Levels adjustment layer"),("BrightnessContrast", 12, "Brightness/Contrast adjustment layer"),("Selection", 13, "Non floating selection"),("FloatingSelection", 14, "Floating selection layer"),("ArtMedia", 15, "Art Media Layer"),("Vibrancy", 16, "Vibrancy adjustment Layer"),("Histogram", 17, "Histogram adjustment layer"),("LocalToneMapping", 18, "Local tone mapping adjustment layer"),("FillLightClarity", 19, "Fill Light/Clarity adjustment Layer"),("SmartFix", 20, "Smart Photo Fix adjustment Layer"),]


        class __Jp2VariantConst(PSPEnumType): 
            '''JPEG 2000 lossless/lossy variant.'''
            Lossy = 0
            Lossless = 1
            def __init__(self):
                self.__name = "Jp2Variant"
                self.__desc = "JPEG 2000 lossless/lossy variant."
                self.__values = [("Lossy", 0, "Lossy JPEG 2000."),("Lossless", 1, "Lossless JPEG 2000."),]


        class __AntialiasTypeConst(PSPEnumType): 
            '''The anti-aliasing type'''
            Inside = 0
            Outside = 1
            def __init__(self):
                self.__name = "AntialiasType"
                self.__desc = "The anti-aliasing type"
                self.__values = [("Inside", 0, "anti-alias the outmost selection pixels"),("Outside", 1, "anti-alias adjacent to selection non selected pixels"),]


        class __Jp2QualityConst(PSPEnumType): 
            '''JPEG 2000 quality method.'''
            Rate = 0
            Size = 1
            def __init__(self):
                self.__name = "Jp2Quality"
                self.__desc = "JPEG 2000 quality method."
                self.__values = [("Rate", 0, "JPEG 2000 compression rate."),("Size", 1, "JPEG 2000 compression size."),]


        class __ChromaSubSamplingConst(PSPEnumType): 
            '''JPEG Chroma Sub-Sampling'''
            YCC_1x1_1x1_1x1 = 0
            YCC_2x1_1x1_1x1 = 1
            YCC_1x2_1x1_1x1 = 2
            YCC_2x2_1x1_1x1 = 3
            YCC_2x2_2x1_2x1 = 4
            YCC_4x2_1x1_1x1 = 5
            YCC_2x4_1x1_1x1 = 6
            YCC_4x1_1x1_1x1 = 7
            YCC_1x4_1x1_1x1 = 8
            YCC_4x1_2x1_2x1 = 9
            YCC_1x4_1x2_1x2 = 10
            YCC_4x4_2x2_2x2 = 11
            def __init__(self):
                self.__name = "ChromaSubSampling"
                self.__desc = "JPEG Chroma Sub-Sampling"
                self.__values = [("YCC_1x1_1x1_1x1", 0, "Luminance: 1x1, Chrominance: 1x1"),("YCC_2x1_1x1_1x1", 1, "Luminance: 2x1, Chrominance: 1x1"),("YCC_1x2_1x1_1x1", 2, "Luminance: 1x2, Chrominance: 1x1"),("YCC_2x2_1x1_1x1", 3, "Luminance: 2x2, Chrominance: 1x1 (default value)"),("YCC_2x2_2x1_2x1", 4, "Luminance: 2x2, Chrominance: 2x1"),("YCC_4x2_1x1_1x1", 5, "Luminance: 4x2, Chrominance: 1x1"),("YCC_2x4_1x1_1x1", 6, "Luminance: 2x4, Chrominance: 1x1"),("YCC_4x1_1x1_1x1", 7, "Luminance: 4x1, Chrominance: 1x1"),("YCC_1x4_1x1_1x1", 8, "Luminance: 1x4, Chrominance: 1x1"),("YCC_4x1_2x1_2x1", 9, "Luminance: 4x1, Chrominance: 2x1"),("YCC_1x4_1x2_1x2", 10, "Luminance: 1x4, Chrominance: 1x2"),("YCC_4x4_2x2_2x2", 11, "Luminance: 4x4, Chrominance: 2x2"),]


        class __ClipboardExitConst(PSPEnumType): 
            '''How data in the clipboard should be handled'''
            Ask = 0
            Delete = 1
            Leave = 2
            def __init__(self):
                self.__name = "ClipboardExit"
                self.__desc = "How data in the clipboard should be handled"
                self.__values = [("Ask", 0, "Ask the user"),("Delete", 1, "Delete the data"),("Leave", 2, "Leave the data"),]


        class __OnOffConst(PSPEnumType): 
            '''Turns feature on, off, or toggles current state.'''
            On = 0
            Off = 1
            Toggle = 2
            def __init__(self):
                self.__name = "OnOff"
                self.__desc = "Turns feature on, off, or toggles current state."
                self.__values = [("On", 0, "Turns feature on"),("Off", 1, "Turns feature off"),("Toggle", 2, "Toggles current state"),]


        class __PromptStateConst(PSPEnumType): 
            '''Prompt state for fixup commands'''
            PSAlwaysDo = 0
            PSNeverDo = 1
            PSAskBeforeDoing = 2
            def __init__(self):
                self.__name = "PromptState"
                self.__desc = "Prompt state for fixup commands"
                self.__values = [("PSAlwaysDo", 0, "Always do"),("PSNeverDo", 1, "Never do"),("PSAskBeforeDoing", 2, "Ask before doing"),]


        class __SaveAllNoneListConst(PSPEnumType): 
            '''Save all dirty files, save no dirty files, or save dirty files in list.'''
            SaveNone = 0
            SaveList = 1
            def __init__(self):
                self.__name = "SaveAllNoneList"
                self.__desc = "Save all dirty files, save no dirty files, or save dirty files in list."
                self.__values = [("SaveNone", 0, "Save none of the dirty files."),("SaveList", 1, "Save dirty files in list."),]


        class __HMSAdjustmentMethodConst(PSPEnumType): 
            '''Adjustment method for highlight, midtone, and shadow values.'''
            Linear = 0
            Dynamic = 1
            def __init__(self):
                self.__name = "HMSAdjustmentMethod"
                self.__desc = "Adjustment method for highlight, midtone, and shadow values."
                self.__values = [("Linear", 0, "Linear HMS adjustment Method"),("Dynamic", 1, "Dynamic HMS adjustment Method"),]


        class __PictureTubeSelectionModeConst(PSPEnumType): 
            '''Specifies in what order cells are selected'''
            Random = 0
            Incremental = 1
            Angular = 2
            Pressure = 3
            Velocity = 4
            def __init__(self):
                self.__name = "PictureTubeSelectionMode"
                self.__desc = "Specifies in what order cells are selected"
                self.__values = [("Random", 0, "Random"),("Incremental", 1, "Incremental"),("Angular", 2, "Angular"),("Pressure", 3, "Pressure"),("Velocity", 4, "Velocity"),]


        class __BackgroundEraserSamplingModeConst(PSPEnumType): 
            '''How to determine the color being erased'''
            Once = 0
            Continuous = 1
            Backswatch = 2
            Foreswatch = 3
            def __init__(self):
                self.__name = "BackgroundEraserSamplingMode"
                self.__desc = "How to determine the color being erased"
                self.__values = [("Once", 0, "Erase only areas containing the color that you first click"),("Continuous", 1, "Sample colors continuously as you drag"),("Backswatch", 2, "Erase only areas containing the current background color"),("Foreswatch", 3, "Erase only areas containing the current foreground color"),]


        class __BackgroundEraserLimitsConst(PSPEnumType): 
            '''How far to let the erasing spread'''
            Discontiguous = 0
            Contiguous = 1
            FindEdges = 2
            def __init__(self):
                self.__name = "BackgroundEraserLimits"
                self.__desc = "How far to let the erasing spread"
                self.__values = [("Discontiguous", 0, "Erase the sampled color wherever it occurs under the brush"),("Contiguous", 1, "Erase areas that contain the sampled color and are connected to one another"),("FindEdges", 2, "Erase connected areas containing the sampled color while better preserving the sharpness of shape edges"),]


        class __RetouchChangeToTargetModesConst(PSPEnumType): 
            '''Changes value to a target value.'''
            Saturation = 0
            Lightness = 1
            Hue = 2
            Color = 3
            def __init__(self):
                self.__name = "RetouchChangeToTargetModes"
                self.__desc = "Changes value to a target value."
                self.__values = [("Saturation", 0, "Applies the saturation value equal to that of the foreground material."),("Lightness", 1, "Applies the lightness value equal to that of the foreground material."),("Hue", 2, "Applies the hue value equal to that of the foreground material."),("Color", 3, "Applies the foreground material color without affecting the luminance."),]


        class __PlacementModeConst(PSPEnumType): 
            '''Defines how items are placed'''
            Random = 0
            Continuous = 1
            def __init__(self):
                self.__name = "PlacementMode"
                self.__desc = "Defines how items are placed"
                self.__values = [("Random", 0, "Random"),("Continuous", 1, "Continuous"),]


        class __RetouchDirectionConst(PSPEnumType): 
            '''Specifies direction of the operation (up or down)'''
            Up = 0
            Down = 1
            def __init__(self):
                self.__name = "RetouchDirection"
                self.__desc = "Specifies direction of the operation (up or down)"
                self.__values = [("Up", 0, "Move values up."),("Down", 1, "Move values down."),]


        class __RetouchLightenDarkenModesConst(PSPEnumType): 
            '''Increases (decreases) lightness or brightness.'''
            RGB = 0
            Lightness = 1
            def __init__(self):
                self.__name = "RetouchLightenDarkenModes"
                self.__desc = "Increases (decreases) lightness or brightness."
                self.__values = [("RGB", 0, "Modifies RGB values."),("Lightness", 1, "Changes lightness values (affects HSL)."),]


        class __RedEyeMethodConst(PSPEnumType): 
            '''Specifies how red eye is selected and fixed.'''
            AutoHumanEye = 0
            AutoAnimalEye = 1
            FreehandPupilOutline = 2
            PointToPointPupilOutline = 3
            def __init__(self):
                self.__name = "RedEyeMethod"
                self.__desc = "Specifies how red eye is selected and fixed."
                self.__values = [("AutoHumanEye", 0, "Auto Human Eye"),("AutoAnimalEye", 1, "Auto Animal Eye"),("FreehandPupilOutline", 2, "Freehand Pupil Outline"),("PointToPointPupilOutline", 3, "Point-to-Point Pupil Outline"),]


        class __SelectionModifyTypeConst(PSPEnumType): 
            '''Specifies how selection should be modified'''
            Custom = 0
            SurroundCurrent = 1
            Opaque = 2
            OpaqueMerged = 3
            def __init__(self):
                self.__name = "SelectionModifyType"
                self.__desc = "Specifies how selection should be modified"
                self.__values = [("Custom", 0, "Custom size and position"),("SurroundCurrent", 1, "Surround current selection"),("Opaque", 2, "Surround opaque area (current layer)"),("OpaqueMerged", 3, "Surround opaque area (merged)"),]


        class __MaskFillConst(PSPEnumType): 
            '''Determines if the area outside of a mask's bitmap image is to be hidden or shown.'''
            Hide = 0
            Show = 1
            FileValue = 2
            def __init__(self):
                self.__name = "MaskFill"
                self.__desc = "Determines if the area outside of a mask's bitmap image is to be hidden or shown."
                self.__values = [("Hide", 0, "Assume area outside of bitmap is hidden."),("Show", 1, "Assume area outside of bitmap is shown."),("FileValue", 2, "Use the show/hide all value saved in the file."),]


        class __MaskLoadOrientationConst(PSPEnumType): 
            '''Determines if loaded mask is to be resized, and to what combination of layer, canvas rects to resize to.'''
            FitToCanvas = 0
            FitToLayer = 1
            AsIs = 2
            def __init__(self):
                self.__name = "MaskLoadOrientation"
                self.__desc = "Determines if loaded mask is to be resized, and to what combination of layer, canvas rects to resize to."
                self.__values = [("FitToCanvas", 0, "Resize to canvas rect."),("FitToLayer", 1, "Resize to current layer rect."),("AsIs", 2, "Load at predetermined position; do not resize."),]


        class __CreateAlphaFromConst(PSPEnumType): 
            '''Determines the source iterator for a new alpha channel layer.'''
            Selection = 0
            Mask = 1
            def __init__(self):
                self.__name = "CreateAlphaFrom"
                self.__desc = "Determines the source iterator for a new alpha channel layer."
                self.__values = [("Selection", 0, "Get from the selection."),("Mask", 1, "Get from the mask."),]


        class __SelectionShapeConst(PSPEnumType): 
            '''Specifies the shape of the geometric selection'''
            Rectangle = 0
            Square = 1
            RoundedRectangle = 2
            RoundedSquare = 3
            Ellipse = 4
            Circle = 5
            Triangle = 6
            Pentagon = 7
            Hexagon = 8
            Octagon = 9
            Star1 = 10
            Star2 = 11
            Arrow1 = 12
            Arrow2 = 13
            Arrow3 = 14
            def __init__(self):
                self.__name = "SelectionShape"
                self.__desc = "Specifies the shape of the geometric selection"
                self.__values = [("Rectangle", 0, "Rectangle"),("Square", 1, "Square"),("RoundedRectangle", 2, "Rounded Rectangle"),("RoundedSquare", 3, "Rounded Square"),("Ellipse", 4, "Ellipse"),("Circle", 5, "Circle"),("Triangle", 6, "Triangle"),("Pentagon", 7, "Pentagon"),("Hexagon", 8, "Hexagon"),("Octagon", 9, "Octagon"),("Star1", 10, "Star 1"),("Star2", 11, "Star 2"),("Arrow1", 12, "Arrow 1"),("Arrow2", 13, "Arrow 2"),("Arrow3", 14, "Arrow 3"),]


        class __SelectionStyleConst(PSPEnumType): 
            '''Specifies the style of the geometric selection'''
            Normal = 0
            FixedSize = 1
            FixedRatio = 2
            def __init__(self):
                self.__name = "SelectionStyle"
                self.__desc = "Specifies the style of the geometric selection"
                self.__values = [("Normal", 0, "Normal"),("FixedSize", 1, "Fixed size"),("FixedRatio", 2, "Fixed Ratio"),]


        class __LayerOrSelectionConst(PSPEnumType): 
            '''Choose to operate on current layer or raster selection'''
            Layer = 0
            Selection = 1
            def __init__(self):
                self.__name = "LayerOrSelection"
                self.__desc = "Choose to operate on current layer or raster selection"
                self.__values = [("Layer", 0, "Operate on currently selected layer"),("Selection", 1, "Operate on raster selection"),]


        class __OrientationConst(PSPEnumType): 
            '''Vector Object Orientation'''
            Normal = 0
            Reversed = 1
            Flipped = 2
            ReverseFlipped = 3
            def __init__(self):
                self.__name = "Orientation"
                self.__desc = "Vector Object Orientation"
                self.__values = [("Normal", 0, "Normal - x,y upper left corner"),("Reversed", 1, "Reversed - x,y upper right corner"),("Flipped", 2, "Flipped - x,y lower left corner"),("ReverseFlipped", 3, "Reverse Flipped - x,y lower right corner"),]


        class __ViewMaskOverlayConst(PSPEnumType): 
            '''Is a color overlay to be displayed for a mask'''
            Enable = 0
            Disable = 1
            Toggle = 2
            def __init__(self):
                self.__name = "ViewMaskOverlay"
                self.__desc = "Is a color overlay to be displayed for a mask"
                self.__values = [("Enable", 0, "Show overlay"),("Disable", 1, "Hide overlay"),("Toggle", 2, "Toggle overlay visibility"),]


        class __ObjectSelectionConst(PSPEnumType): 
            '''These are the enumerations for the object selection scripting'''
            Select = 0
            AddToSelection = 1
            RemoveFromSelection = 2
            def __init__(self):
                self.__name = "ObjectSelection"
                self.__desc = "These are the enumerations for the object selection scripting"
                self.__values = [("Select", 0, "Create a completely new selection for objects."),("AddToSelection", 1, "Add an object to the current selection."),("RemoveFromSelection", 2, "Remove the current object from the selection."),]


        class __MaterialRefConst(PSPEnumType): 
            '''Which Material is being referenced (Foreground/Stroke or Background/Fill)'''
            Foreground = 0
            Background = 1
            def __init__(self):
                self.__name = "MaterialRef"
                self.__desc = "Which Material is being referenced (Foreground/Stroke or Background/Fill)"
                self.__values = [("Foreground", 0, "Foreground/Stroke Material"),("Background", 1, "Background/Fill Material"),]


        class __PixelFormatConst(PSPEnumType): 
            '''Describes raster image pixel format.'''
            Custom = -1
            Undefined = 0
            Index1 = 1
            Index4 = 2
            Index8 = 3
            Index8A = 4
            Grey = 5
            GreyA = 6
            BGR = 7
            BGRA = 8
            BGRxA = 9
            Grey_u16 = 10
            GreyA_u16 = 11
            BGR_u16 = 12
            BGRA_u16 = 13
            BGRxA_u16 = 14
            Grey_f32 = 15
            GreyA_f32 = 16
            BGR_f32 = 17
            BGRA_f32 = 18
            BGRxA_f32 = 19
            def __init__(self):
                self.__name = "PixelFormat"
                self.__desc = "Describes raster image pixel format."
                self.__values = [("Custom", -1, "Custom pixel format."),("Undefined", 0, "Undefined or no pixel format."),("Index1", 1, "1-bit index into palette"),("Index4", 2, "4-bit index into palette"),("Index8", 3, "8-bit index into palette"),("Index8A", 4, "8-bit index into palette with alpha"),("Grey", 5, "8-bit Grey"),("GreyA", 6, "16-bit Grey with Alpha"),("BGR", 7, "24-bit RGB"),("BGRA", 8, "32-bit RGBA"),("BGRxA", 9, "32-bit RGBA with premultiplied alpha"),("Grey_u16", 10, "8-bit Grey_u16"),("GreyA_u16", 11, "16-bit Grey_u16 with Alpha"),("BGR_u16", 12, "24-bit RGB_u16"),("BGRA_u16", 13, "32-bit RGBA_u16"),("BGRxA_u16", 14, "32-bit RGBA_u16 with premultiplied alpha"),("Grey_f32", 15, "8-bit Grey_f32"),("GreyA_f32", 16, "16-bit Grey_f32 with Alpha"),("BGR_f32", 17, "24-bit RGB_f32"),("BGRA_f32", 18, "32-bit RGBA_f32"),("BGRxA_f32", 19, "32-bit RGBA_f32 with premultiplied alpha"),]


        class __PrintPagePositionConst(PSPEnumType): 
            '''Determines the position of the image on the page.'''
            FitPage = 0
            CenterPage = 1
            UpperLeftPage = 2
            OffsetPage = 3
            def __init__(self):
                self.__name = "PrintPagePosition"
                self.__desc = "Determines the position of the image on the page."
                self.__values = [("FitPage", 0, "Centers and scales the image to fit the page."),("CenterPage", 1, "Centers the image on the page."),("UpperLeftPage", 2, "Positions image in the upper left corner."),("OffsetPage", 3, "Positions image according to top left offsets."),]


        class __PrintRangeConst(PSPEnumType): 
            '''Print all pages, page range, or selection.'''
            All = 0
            Range = 1
            Selection = 2
            def __init__(self):
                self.__name = "PrintRange"
                self.__desc = "Print all pages, page range, or selection."
                self.__values = [("All", 0, "Print all pages."),("Range", 1, "Print page range."),("Selection", 2, "Print selection."),]


        class __PathEntryInterpretationConst(PSPEnumType): 
            '''How to interpret an entry on a path.'''
            Absolute = 0
            def __init__(self):
                self.__name = "PathEntryInterpretation"
                self.__desc = "How to interpret an entry on a path."
                self.__values = [("Absolute", 0, "Entry contains absolute values."),]


        class __VarianceMethodConst(PSPEnumType): 
            '''Method by which to vary a brush setting.'''
            None = 0
            Pressure = 1
            TiltAngle = 2
            TiltDirection = 3
            Orientation = 4
            Fingerwheel = 5
            ZWheel = 6
            Direction = 7
            FadeIn = 8
            RepeatingFadeIn = 9
            FadeOut = 10
            OscillatingFade = 11
            Altitude = 2
            Azimuth = 3
            Twist = 4
            def __init__(self):
                self.__name = "VarianceMethod"
                self.__desc = "Method by which to vary a brush setting."
                self.__values = [("None", 0, "Setting does not vary."),("Pressure", 1, "Vary setting by tool pressure."),("TiltAngle", 2, "Vary setting by tool tilt angle."),("TiltDirection", 3, "Vary setting by tool tilt direction."),("Orientation", 4, "Vary setting by tool orientation or rotation about its center."),("Fingerwheel", 5, "Vary setting by fingerwheel."),("ZWheel", 6, "Vary setting by tool z-wheel."),("Direction", 7, "Vary setting by stroke direction."),("FadeIn", 8, "Fade setting in over duration of pixel fade value."),("RepeatingFadeIn", 9, "Repeatedly fade setting in over duration of pixel fade value."),("FadeOut", 10, "Fade setting out over duration of pixel fade value."),("OscillatingFade", 11, "Repeatedly fade setting in over the over duration of pixel fade value, and then fade out over same duration."),("Altitude", 2, "Vary setting by tool tilt angle."),("Azimuth", 3, "Vary setting by tool tilt direction."),("Twist", 4, "Vary setting by tool orientation or rotation about its center."),]


        class __JointStyleConst(PSPEnumType): 
            '''The joint style of the preset shape'''
            Miter = 0
            Round = 1
            Bevel = 2
            def __init__(self):
                self.__name = "JointStyle"
                self.__desc = "The joint style of the preset shape"
                self.__values = [("Miter", 0, "Miter joint style"),("Round", 1, "Round joint style"),("Bevel", 2, "Bevel joint style"),]


        class __CreateAsConst(PSPEnumType): 
            '''Create the text as the following type; vector, selection or floating.'''
            Vector = 0
            Selection = 1
            Floating = 2
            def __init__(self):
                self.__name = "CreateAs"
                self.__desc = "Create the text as the following type; vector, selection or floating."
                self.__values = [("Vector", 0, "Create text as vector."),("Selection", 1, "Create text as selection."),("Floating", 2, "Create text as floating."),]


        class __FontSizeUnitsConst(PSPEnumType): 
            '''Font size units; points or pixels'''
            Points = 0
            Pixels = 1
            def __init__(self):
                self.__name = "FontSizeUnits"
                self.__desc = "Font size units; points or pixels"
                self.__values = [("Points", 0, "Font size is in points."),("Pixels", 1, "Font size is in pixels."),]


        class __TextTypeConst(PSPEnumType): 
            '''Defines whether text is attached to an object or simply a baseline start position'''
            TextBase = 0
            TextPath = 1
            def __init__(self):
                self.__name = "TextType"
                self.__desc = "Defines whether text is attached to an object or simply a baseline start position"
                self.__values = [("TextBase", 0, "Text uses a baseline start position."),("TextPath", 1, "Text is attached to an object."),]


        class __JustifyConst(PSPEnumType): 
            '''Defines how to justify text; left, right, or center.'''
            Left = 0
            Right = 1
            Center = 2
            Justification = 3
            FullJustification = 4
            def __init__(self):
                self.__name = "Justify"
                self.__desc = "Defines how to justify text; left, right, or center."
                self.__values = [("Left", 0, "Left justify text"),("Right", 1, "Right justify text"),("Center", 2, "Center justify text"),("Justification", 3, ""),("FullJustification", 4, ""),]


        class __ColorRangeActionConst(PSPEnumType): 
            '''Controls the Add/Subtract Color Range effect behaviour'''
            Add = 0
            Subtract = 1
            def __init__(self):
                self.__name = "ColorRangeAction"
                self.__desc = "Controls the Add/Subtract Color Range effect behaviour"
                self.__values = [("Add", 0, "Add color range to selection"),("Subtract", 1, "Subtract color range from a selection"),]


        class __BubbleCreateMethodConst(PSPEnumType): 
            '''Method of bubble creation'''
            Overlapping = 0
            NonIntersecting = 1
            Intersecting = 2
            def __init__(self):
                self.__name = "BubbleCreateMethod"
                self.__desc = "Method of bubble creation"
                self.__values = [("Overlapping", 0, "Filter will draw  overlapping bubbles"),("NonIntersecting", 1, "Filter will draw non-intersecting bubbles"),("Intersecting", 2, "Filter will draw intersect bubbles "),]


        class __FeatheringTypeConst(PSPEnumType): 
            '''Controls type of feathering that is done'''
            InsideFeathering = 0
            OutsideFeathering = 1
            BothsideFeathering = 2
            def __init__(self):
                self.__name = "FeatheringType"
                self.__desc = "Controls type of feathering that is done"
                self.__values = [("InsideFeathering", 0, "Inside Feathering"),("OutsideFeathering", 1, "Outside Feathering"),("BothsideFeathering", 2, "Bothside Feathering"),]


        class __RemoveSpecksHolesTypeConst(PSPEnumType): 
            '''Controls what is removed by the remove specks and holes selection modifier.'''
            RemoveSpecks = 0
            RemoveHoles = 1
            RemoveSpecksAndHoles = 2
            def __init__(self):
                self.__name = "RemoveSpecksHolesType"
                self.__desc = "Controls what is removed by the remove specks and holes selection modifier."
                self.__values = [("RemoveSpecks", 0, "Specks"),("RemoveHoles", 1, "Holes"),("RemoveSpecksAndHoles", 2, "Specks And Holes"),]


        class __WarpingBrushModeConst(PSPEnumType): 
            '''Describes one of eight Warping Brush modes.'''
            Push = 0
            Expand = 1
            Contract = 2
            RightTwirl = 3
            LeftTwirl = 4
            Noise = 5
            IronOut = 6
            Unwarp = 7
            def __init__(self):
                self.__name = "WarpingBrushMode"
                self.__desc = "Describes one of eight Warping Brush modes."
                self.__values = [("Push", 0, "Push mode"),("Expand", 1, "Expand mode"),("Contract", 2, "Contract mode"),("RightTwirl", 3, "Right Twirl mode"),("LeftTwirl", 4, "Left Twirl mode"),("Noise", 5, "Noise mode"),("IronOut", 6, "IronOut mode"),("Unwarp", 7, "Unwarp mode"),]


        class __BubbleMapTypeConst(PSPEnumType): 
            '''What is mapped on the bubble surface'''
            Diffraction = 0
            CurrentImage = 1
            Environment = 2
            def __init__(self):
                self.__name = "BubbleMapType"
                self.__desc = "What is mapped on the bubble surface"
                self.__values = [("Diffraction", 0, "Diffraction map"),("CurrentImage", 1, "Current Image as Environment map"),("Environment", 2, "Environment map"),]


        class __CountTypeConst(PSPEnumType): 
            '''Number of objects'''
            Single = 0
            Multiple = 1
            def __init__(self):
                self.__name = "CountType"
                self.__desc = "Number of objects"
                self.__values = [("Single", 0, "Single object"),("Multiple", 1, "Multiple objects"),]


        class __LensFrameShapeConst(PSPEnumType): 
            '''Shape of the lens frame'''
            Circular = 0
            RoundedSquare = 1
            def __init__(self):
                self.__name = "LensFrameShape"
                self.__desc = "Shape of the lens frame"
                self.__values = [("Circular", 0, "Circular lens frame"),("RoundedSquare", 1, "Rounded square lens frame"),]


        class __LensFrameMaterialConst(PSPEnumType): 
            '''Material of the lens frame'''
            None = 0
            Chrome = 1
            Gold = 2
            BrightBronze = 3
            RedBronze = 4
            DullBronze = 5
            Ceramic = 6
            ShinyBluePlastic = 7
            DullRedPlastic = 8
            BeigePlastic = 9
            BlackPlastic = 10
            BrownPlastic = 11
            ClearPlastic = 12
            Silver = 13
            def __init__(self):
                self.__name = "LensFrameMaterial"
                self.__desc = "Material of the lens frame"
                self.__values = [("None", 0, "No frame"),("Chrome", 1, "Chrome frame"),("Gold", 2, "Gold frame"),("BrightBronze", 3, "Bright Bronze frame"),("RedBronze", 4, "Red Bronze frame"),("DullBronze", 5, "Dull Bronze frame"),("Ceramic", 6, "Ceramic frame"),("ShinyBluePlastic", 7, "Shiny blue plastic frame"),("DullRedPlastic", 8, "Dull red plastic frame"),("BeigePlastic", 9, "Beige plastic frame"),("BlackPlastic", 10, "Black plastic frame"),("BrownPlastic", 11, "Brown plastic frame"),("ClearPlastic", 12, "Clear plastic frame"),("Silver", 13, "Silver frame"),]


        class __LensShapeConst(PSPEnumType): 
            '''Type of lens shape'''
            Spherical = 0
            VCylindrical = 1
            HCylindrical = 2
            def __init__(self):
                self.__name = "LensShape"
                self.__desc = "Type of lens shape"
                self.__values = [("Spherical", 0, "Spherical lens"),("VCylindrical", 1, "Cylindrical vertical lens"),("HCylindrical", 2, "Cylindrical horizontal lens"),]


        class __RotateModeConst(PSPEnumType): 
            '''Mode of rotating an image in the rotate warping command'''
            Auto = 0
            Vertical = 1
            Horizontal = 2
            def __init__(self):
                self.__name = "RotateMode"
                self.__desc = "Mode of rotating an image in the rotate warping command"
                self.__values = [("Auto", 0, "Automatic adjustment"),("Vertical", 1, "Make the guideline vertical"),("Horizontal", 2, "Make the guideline horizontal"),]


        class __BordersTypeConst(PSPEnumType): 
            '''Controls how a selection border is defined.'''
            Inside = 0
            Outside = 1
            BothSide = 2
            def __init__(self):
                self.__name = "BordersType"
                self.__desc = "Controls how a selection border is defined."
                self.__values = [("Inside", 0, "Select borders inside the initial selection"),("Outside", 1, "Select borders outside the initial selection"),("BothSide", 2, "Select borders around the initial selection border"),]


        class __TileShapeConst(PSPEnumType): 
            '''Shape to use for the Tiles effect'''
            Triangle = 0
            Square = 1
            Hexagon = 2
            def __init__(self):
                self.__name = "TileShape"
                self.__desc = "Shape to use for the Tiles effect"
                self.__values = [("Triangle", 0, "A Tiles effect shape"),("Square", 1, "A Tiles effect shape"),("Hexagon", 2, "A Tiles effect shape"),]


        class __CreateMaskFromConst(PSPEnumType): 
            '''Source for mask's creation'''
            Luminance = 0
            NonZero = 1
            Opacity = 2
            def __init__(self):
                self.__name = "CreateMaskFrom"
                self.__desc = "Source for mask's creation"
                self.__values = [("Luminance", 0, "Source Luminance"),("NonZero", 1, "Any non-zero value"),("Opacity", 2, "Source opacity"),]


        class __WpgVersionConst(PSPEnumType): 
            '''WPG (WordPerfect Bitmap) file format version.'''
            WPG50 = 0
            WPG51 = 1
            WPG60 = 2
            def __init__(self):
                self.__name = "WpgVersion"
                self.__desc = "WPG (WordPerfect Bitmap) file format version."
                self.__values = [("WPG50", 0, "WPG Version 5.0"),("WPG51", 1, "WPG Version 5.1"),("WPG60", 2, "WPG Version 6.0"),]


        class __TgaColorsConst(PSPEnumType): 
            '''TGA (TrueVision Targa) bit-depth encoding.'''
            TGA8 = 0
            TGA16 = 1
            TGA24 = 2
            def __init__(self):
                self.__name = "TgaColors"
                self.__desc = "TGA (TrueVision Targa) bit-depth encoding."
                self.__values = [("TGA8", 0, "8 bits TGA"),("TGA16", 1, "16 bits TGA"),("TGA24", 2, "24 bits TGA"),]


        class __SctChannelsConst(PSPEnumType): 
            '''SCT (SciTex Continuous Tone) color channel encoding.'''
            CMY = 0
            CMYK = 1
            def __init__(self):
                self.__name = "SctChannels"
                self.__desc = "SCT (SciTex Continuous Tone) color channel encoding."
                self.__values = [("CMY", 0, "CMY Planes Encoding"),("CMYK", 1, "CMYK Planes Encoding"),]


        class __RleFormatConst(PSPEnumType): 
            '''Windows or CompuServe RLE sub-format type.'''
            CompuServe = 0
            Windows = 1
            def __init__(self):
                self.__name = "RleFormat"
                self.__desc = "Windows or CompuServe RLE sub-format type."
                self.__values = [("CompuServe", 0, "CompuServe RLE Format"),("Windows", 1, "Windows RLE Format"),]


        class __PspVersionConst(PSPEnumType): 
            '''PSP file format version.'''
            PSP5 = 0
            PSP6 = 1
            PSP7 = 2
            PSP8 = 3
            PSP9 = 4
            PSP10 = 5
            PSP11 = 6
            PSP12 = 7
            PSP13 = 8
            PSP14 = 9
            PSP18 = 10
            def __init__(self):
                self.__name = "PspVersion"
                self.__desc = "PSP file format version."
                self.__values = [("PSP5", 0, "PSP 5 compatible file"),("PSP6", 1, "PSP 6 compatible file"),("PSP7", 2, "PSP 7 compatible file"),("PSP8", 3, "PSP 8 compatible file"),("PSP9", 4, "PSP 9 compatible file"),("PSP10", 5, "PSP 10 compatible file"),("PSP11", 6, "PSP 11 compatible file"),("PSP12", 7, "PSP 12 compatible file"),("PSP13", 8, "PSP X3 compatible file"),("PSP14", 9, "PSP X4 - X7 compatible file"),("PSP18", 10, "PSP X8 - 2021 compatible file"),]


        class __PspCompressionConst(PSPEnumType): 
            '''PSP file format compression.'''
            LZ77 = 0
            RLE = 1
            Uncompressed = 2
            def __init__(self):
                self.__name = "PspCompression"
                self.__desc = "PSP file format compression."
                self.__values = [("LZ77", 0, "LZ77 Compression"),("RLE", 1, "RLE Compression"),("Uncompressed", 2, "Uncompressed"),]


        class __PcxVersionConst(PSPEnumType): 
            '''PCX (Zsoft Paintbrush) file format version.'''
            PCX0 = 0
            PCX2 = 1
            PCX5 = 2
            def __init__(self):
                self.__name = "PcxVersion"
                self.__desc = "PCX (Zsoft Paintbrush) file format version."
                self.__values = [("PCX0", 0, "PCX Version 0"),("PCX2", 1, "PCX Version 2"),("PCX5", 2, "PCX Version 5"),]


        class __DataEncodingConst(PSPEnumType): 
            '''File format data encoding.'''
            Ascii = 0
            Binary = 1
            def __init__(self):
                self.__name = "DataEncoding"
                self.__desc = "File format data encoding."
                self.__values = [("Ascii", 0, "Ascii Encoding"),("Binary", 1, "Binary Encoding"),]


        class __GifVersionConst(PSPEnumType): 
            '''GIF file format version.'''
            Gif87a = 0
            Gif89a = 1
            def __init__(self):
                self.__name = "GifVersion"
                self.__desc = "GIF file format version."
                self.__values = [("Gif87a", 0, "GIF Version 87a"),("Gif89a", 1, "GIF Version 89a"),]


        class __BmpFormatConst(PSPEnumType): 
            '''Windows or OS/2 Bitmap (BMP) sub-format type.'''
            OS2 = 0
            Windows = 1
            def __init__(self):
                self.__name = "BmpFormat"
                self.__desc = "Windows or OS/2 Bitmap (BMP) sub-format type."
                self.__values = [("OS2", 0, "OS/2 BMP Format"),("Windows", 1, "Windows BMP Format"),]


        class __VerticalTypeConst(PSPEnumType): 
            '''Vertical placement of the image.'''
            Undefined = 0
            Center = 1
            Top = 2
            Bottom = 3
            Custom = 4
            def __init__(self):
                self.__name = "VerticalType"
                self.__desc = "Vertical placement of the image."
                self.__values = [("Undefined", 0, "Undefined"),("Center", 1, "Center"),("Top", 2, "Top"),("Bottom", 3, "Bottom"),("Custom", 4, "Custom"),]


        class __HorizontalTypeConst(PSPEnumType): 
            '''Horizontal placement of an image on the canvas'''
            Undefined = 0
            Center = 1
            Left = 2
            Right = 3
            Custom = 4
            def __init__(self):
                self.__name = "HorizontalType"
                self.__desc = "Horizontal placement of an image on the canvas"
                self.__values = [("Undefined", 0, "Undefined"),("Center", 1, "Center image in canvas"),("Left", 2, "Align image at left edge of canvas"),("Right", 3, "Align image at right edge of canvas"),("Custom", 4, "Custom alignment"),]


        class __MsgButtonsConst(PSPEnumType): 
            '''Define which buttons should be placed on a message box.'''
            OK = 0
            OKCancel = 1
            YesNo = 2
            def __init__(self):
                self.__name = "MsgButtons"
                self.__desc = "Define which buttons should be placed on a message box."
                self.__values = [("OK", 0, "OK button only"),("OKCancel", 1, "OK and Cancel Buttons (default OK)"),("YesNo", 2, "Yes and No Buttons (default Yes)"),]


        class __MsgIconsConst(PSPEnumType): 
            '''Define the icon to place on a message box'''
            Stop = 0
            Info = 1
            Question = 2
            def __init__(self):
                self.__name = "MsgIcons"
                self.__desc = "Define the icon to place on a message box"
                self.__values = [("Stop", 0, "Stop sign icon"),("Info", 1, "Information icon"),("Question", 2, "Question mark icon"),]


        class __BrushShapeConst(PSPEnumType): 
            '''The shape of the brush tip.'''
            Round = 0
            Rectangular = 1
            Custom = 2
            def __init__(self):
                self.__name = "BrushShape"
                self.__desc = "The shape of the brush tip."
                self.__values = [("Round", 0, "Round brush"),("Rectangular", 1, "Rectangular brush"),("Custom", 2, "Custom brush"),]


        class __SelectionOperationConst(PSPEnumType): 
            '''Specifies if new selection should replace previous one, be added to or removed from it.'''
            Replace = 0
            Add = 1
            Remove = 2
            def __init__(self):
                self.__name = "SelectionOperation"
                self.__desc = "Specifies if new selection should replace previous one, be added to or removed from it."
                self.__values = [("Replace", 0, "New selection is the selection."),("Add", 1, "New selection is added to the existing."),("Remove", 2, "New selection is removed from the existing."),]


        class __FreehandSelectionTypeConst(PSPEnumType): 
            '''Type of the freehand selection'''
            Default = 0
            Freehand = 1
            PointToPoint = 2
            SmartEdge = 3
            EdgeSeeker = 4
            def __init__(self):
                self.__name = "FreehandSelectionType"
                self.__desc = "Type of the freehand selection"
                self.__values = [("Default", 0, "Use default selection type"),("Freehand", 1, "Freehand Selection"),("PointToPoint", 2, "Selection consists of stright lines"),("SmartEdge", 3, "Selection is based on the border between two areas of contrasting color or light"),("EdgeSeeker", 4, "Selection is based on the border between two areas of contrasting color or light"),]


        class __DistortionTypeConst(PSPEnumType): 
            '''Type of lens distortion'''
            Pincushion = 0
            Barrel = 1
            Fisheye = 2
            Spherical = 3
            def __init__(self):
                self.__name = "DistortionType"
                self.__desc = "Type of lens distortion"
                self.__values = [("Pincushion", 0, "Pincushion Effect"),("Barrel", 1, "Barrel Effect"),("Fisheye", 2, "Fisheye Effect"),("Spherical", 3, "Fisheye Effect (equi-scale)"),]


        class __ResampleTypeConst(PSPEnumType): 
            '''Choices for resampling an image'''
            Undefined = 0
            SmartSize = 1
            Bicubic = 2
            Bilinear = 3
            PixelResize = 4
            WeightedAverage = 5
            def __init__(self):
                self.__name = "ResampleType"
                self.__desc = "Choices for resampling an image"
                self.__values = [("Undefined", 0, "No type specified."),("SmartSize", 1, "Use Smart Size to Resample"),("Bicubic", 2, "Use Bicubic interpolation to Resample"),("Bilinear", 3, "Use Bilinear interpolation to Resample"),("PixelResize", 4, "Use Pixel Resize (Nearest Neighbor) to Resize"),("WeightedAverage", 5, "Use Weighted Average to Resample"),]


        class __TransparencyTypeConst(PSPEnumType): 
            '''Type of transparency'''
            NoTransparency = 0
            SingleTransparency = 1
            AlphaTransparency = 2
            def __init__(self):
                self.__name = "TransparencyType"
                self.__desc = "Type of transparency"
                self.__values = [("NoTransparency", 0, "no transparency"),("SingleTransparency", 1, "single color transparency"),("AlphaTransparency", 2, "alpha channel transparency"),]


        class __ImageTypeConst(PSPEnumType): 
            '''Type of image - paletted, greyscale, or true color'''
            Paletted = 0
            Greyscale = 1
            TrueColor = 2
            def __init__(self):
                self.__name = "ImageType"
                self.__desc = "Type of image - paletted, greyscale, or true color"
                self.__values = [("Paletted", 0, "paletted image"),("Greyscale", 1, "greyscale image"),("TrueColor", 2, "true color image"),]


        class __VersionConst(PSPEnumType): 
            '''GIF file format version'''
            Version87a = 0
            Version89a = 1
            def __init__(self):
                self.__name = "Version"
                self.__desc = "GIF file format version"
                self.__values = [("Version87a", 0, "87a"),("Version89a", 1, "89a"),]


        class __SubFormatConst(PSPEnumType): 
            '''Subtype of file; either interlaced or non-interlaced'''
            NonInterlaced = 0
            Interlaced = 1
            def __init__(self):
                self.__name = "SubFormat"
                self.__desc = "Subtype of file; either interlaced or non-interlaced"
                self.__values = [("NonInterlaced", 0, "non interlaced format"),("Interlaced", 1, "interlaced format"),]


        class __ColorSelectionConst(PSPEnumType): 
            '''Method of palette generation'''
            ExistingPalette = 0
            StandardPalette = 1
            OptimizedMedianCutPalette = 2
            OptimizedOctreePalette = 3
            def __init__(self):
                self.__name = "ColorSelection"
                self.__desc = "Method of palette generation"
                self.__values = [("ExistingPalette", 0, "Use existing palette"),("StandardPalette", 1, "Use a standard/web-safe palette"),("OptimizedMedianCutPalette", 2, "Use palette generated by median-cut"),("OptimizedOctreePalette", 3, "Use octree generated palette"),]


        class __PartialTransparencyConst(PSPEnumType): 
            '''Defines handling of partially transparent pixels'''
            FullTransparency = 0
            Dither50Percent = 1
            ErrorDiffusion = 2
            def __init__(self):
                self.__name = "PartialTransparency"
                self.__desc = "Defines handling of partially transparent pixels"
                self.__values = [("FullTransparency", 0, "make full transparent"),("Dither50Percent", 1, "use 50% dither pattern"),("ErrorDiffusion", 2, "use error diffusion dither pattern"),]


        class __TransparencyConst(PSPEnumType): 
            '''Type of transparency'''
            None = 0
            Existing = 1
            InsideSelection = 2
            OutsideSelection = 3
            MatchColor = 4
            ExistingAlpha = 5
            def __init__(self):
                self.__name = "Transparency"
                self.__desc = "Type of transparency"
                self.__values = [("None", 0, "no transparency"),("Existing", 1, "existing image or layer"),("InsideSelection", 2, "inside the current selection"),("OutsideSelection", 3, "outside the current selection"),("MatchColor", 4, "match a defined color"),("ExistingAlpha", 5, "existing alpha channel"),]


        class __ColorSchemeConst(PSPEnumType): 
            '''Halftone effect color scheme'''
            RGB = 0
            Greyscale = 1
            def __init__(self):
                self.__name = "ColorScheme"
                self.__desc = "Halftone effect color scheme"
                self.__values = [("RGB", 0, "Red, green, blue scheme"),("Greyscale", 1, "Greyscale scheme"),]


        class __HalftonePatternConst(PSPEnumType): 
            '''Pattern of the halftoning effect.'''
            Round = 0
            Line = 1
            Square = 2
            def __init__(self):
                self.__name = "HalftonePattern"
                self.__desc = "Pattern of the halftoning effect."
                self.__values = [("Round", 0, "Round pattern"),("Line", 1, "Line pattern"),("Square", 2, "Square pattern"),]


        class __BlendModeConst(PSPEnumType): 
            '''Controls how two layers are blended together.  The upper layer merges itself with the lower layer using the blend mode.'''
            Normal = 0
            Darken = 1
            Lighten = 2
            LegacyHue = 3
            LegacySaturation = 4
            LegacyColor = 5
            LegacyLuminance = 6
            Multiply = 7
            Screen = 8
            Dissolve = 9
            Overlay = 10
            HardLight = 11
            SoftLight = 12
            Difference = 13
            Dodge = 14
            Burn = 15
            Exclusion = 16
            TrueHue = 17
            TrueSaturation = 18
            TrueColor = 19
            TrueLuminance = 20
            PaintBehind = 21
            def __init__(self):
                self.__name = "BlendMode"
                self.__desc = "Controls how two layers are blended together.  The upper layer merges itself with the lower layer using the blend mode."
                self.__values = [("Normal", 0, "Pixels on the current layer are blended with the underlying layer based on opacity."),("Darken", 1, "Each pixel is the darkest of the two layers"),("Lighten", 2, "The lighter pixel of the two layers is displayed"),("LegacyHue", 3, "Applies the hue of the upper layer to the lower layer (legacy)"),("LegacySaturation", 4, "Applies the saturation value of the upper layer to the lower layer (legacy)"),("LegacyColor", 5, "Applies the hue and saturation of the upper layer to the lower layer, preserving the luminance"),("LegacyLuminance", 6, "Applies the luminance of the upper layer to the lower layer, without affecting the color. (legacy)"),("Multiply", 7, "Combines the upper layer with the lower layer to produce a darker color."),("Screen", 8, "Lighten the underlying color by multiplying the inverse of the base and blend colors."),("Dissolve", 9, "Randomly choose either the upper layer pixel or the lower layer pixel.  The probability of picking a pixel is controlled by the opacity."),("Overlay", 10, "Combines multiply and screen modes to preserve the patterns and colors of the upper layer with shadows and highlights from the lower layer."),("HardLight", 11, "Combines multiply and screen modes to add highlights or shadows "),("SoftLight", 12, "Combines burn and dodge modes to create soft shadows and highlights"),("Difference", 13, "Subtracts the lighter pixel from the darker pixel"),("Dodge", 14, "Use the lightness value from the upper layer to lighten colors in the lower layer"),("Burn", 15, "The lightness of the upper layer is used to darken pixels on the lower layer."),("Exclusion", 16, "Creates an effect similar to but softer than the difference mode."),("TrueHue", 17, "Applies the hue of the upper layer to the lower layer"),("TrueSaturation", 18, "Applies the saturation value of the upper layer to the lower layer"),("TrueColor", 19, "Applies the hue and saturation of the upper layer to the lower layer, preserving the luminance"),("TrueLuminance", 20, "Applies the lightness of the upper layer to the lower layer, without affecting the color."),("PaintBehind", 21, "Paints in only transparent areas."),]


        class __PageSizeConst(PSPEnumType): 
            '''Size and type of paper output'''
            Letter = 0
            Legal = 1
            Tabloid = 2
            A3 = 3
            A4 = 4
            B4 = 5
            B5 = 6
            def __init__(self):
                self.__name = "PageSize"
                self.__desc = "Size and type of paper output"
                self.__values = [("Letter", 0, "Letter (8.5 x 11 inches)"),("Legal", 1, "Legal (8.5 x 14 inches)"),("Tabloid", 2, "Tabloid (11 x 17 inches)"),("A3", 3, "A3 (297 x 420 mm)"),("A4", 4, "A4 (210 x 297 mm)"),("B4", 5, "B4 (257 x 364 mm)"),("B5", 6, "B5 (182 x 254 mm)"),]


        class __DisplacementMapTypeConst(PSPEnumType): 
            '''Type of displacement maps'''
            Preset = 0
            File = 1
            Image = 2
            def __init__(self):
                self.__name = "DisplacementMapType"
                self.__desc = "Type of displacement maps"
                self.__values = [("Preset", 0, "Displacement map is preset displacement map"),("File", 1, "Displacement map is a local file"),("Image", 2, "Displacement map is an open image"),]


        class __DisplacementLayoutConst(PSPEnumType): 
            '''Displacement layout'''
            Tile = 0
            Stretch = 1
            def __init__(self):
                self.__name = "DisplacementLayout"
                self.__desc = "Displacement layout"
                self.__values = [("Tile", 0, "Tile displacement map to cover source image"),("Stretch", 1, "Stretch displacement map to cover source image"),]


        class __RadialBlurTypeConst(PSPEnumType): 
            '''Type of radial blur'''
            Spin = 0
            Zoom = 1
            Twirl = 2
            def __init__(self):
                self.__name = "RadialBlurType"
                self.__desc = "Type of radial blur"
                self.__values = [("Spin", 0, "Blur has effect of spinning image about center"),("Zoom", 1, "Blur has effect of rapidly zooming on center"),("Twirl", 2, "Zoom has effect of blurring and twirling image"),]


        class __CAMGEngineTypeConst(PSPEnumType): 
            '''CAMGEngineType'''
            Segmentation = 1
            MagicWand = 2
            ObjectExtractor = 3
            def __init__(self):
                self.__name = "CAMGEngineType"
                self.__desc = "CAMGEngineType"
                self.__values = [("Segmentation", 1, "CAMG Engine uses Segmentation engine"),("MagicWand", 2, "CAMG engine uses MagicWand engine"),("ObjectExtractor", 3, "CAMG Engine uses ObjectExtractor engine"),]


        class __TiffCompressionConst(PSPEnumType): 
            '''TIFF compression types'''
            None = 0
            FAX = 1
            Huffman = 2
            LZW = 3
            Packbits = 4
            def __init__(self):
                self.__name = "TiffCompression"
                self.__desc = "TIFF compression types"
                self.__values = [("None", 0, "Uncompressed"),("FAX", 1, "Conforms to CCITT-3 (facsimile)"),("Huffman", 2, "Conforms to Huffman format (lossless)"),("LZW", 3, "Conforms to Lempel-Ziv format (lossless)"),("Packbits", 4, "Subset of Postscript level 2"),]


        class __ColorChannelsConst(PSPEnumType): 
            '''Colorspace of the image'''
            RGB = 0
            CMYK = 1
            LAB = 2
            YCC = 3
            def __init__(self):
                self.__name = "ColorChannels"
                self.__desc = "Colorspace of the image"
                self.__values = [("RGB", 0, "Red|Green|Blue color"),("CMYK", 1, "Cyan|Magenta|Yellow|blacK, for printer color matching"),("LAB", 2, "L*a*b colorspace"),("YCC", 3, "YCrCb colorspace, used in video images"),]


        class __JpegEncodingConst(PSPEnumType): 
            '''Encoding format for JPEG compression'''
            Standard = 0
            Progressive = 1
            JPEG2000 = 2
            def __init__(self):
                self.__name = "JpegEncoding"
                self.__desc = "Encoding format for JPEG compression"
                self.__values = [("Standard", 0, "Most compatible format"),("Progressive", 1, "Interlaced image, for web images"),("JPEG2000", 2, "JPEG 2000 compatible, most compression"),]


        class __ColorOrderConst(PSPEnumType): 
            '''Order of color bits in RAW format'''
            RGB = 0
            BGR = 1
            def __init__(self):
                self.__name = "ColorOrder"
                self.__desc = "Order of color bits in RAW format"
                self.__values = [("RGB", 0, "Red|Green|Blue order"),("BGR", 1, "Blue|Green|Red order"),]


        class __ImageModeConst(PSPEnumType): 
            '''Default color mode of image.'''
            Monochrome = 0
            Greyscale = 1
            RGB = 2
            CMYK = 3
            LAB = 4
            YCC = 5
            def __init__(self):
                self.__name = "ImageMode"
                self.__desc = "Default color mode of image."
                self.__values = [("Monochrome", 0, "Monochrome (1-bit)"),("Greyscale", 1, "Greyscale (8-bit)"),("RGB", 2, "RGB (24-bit)"),("CMYK", 3, "Cyan|Magenta|Yellow|blacK, for printer color matching"),("LAB", 4, "L*a*b colorspace"),("YCC", 5, "YCrCb color space, used in video images"),]


        class __ImageSizeConst(PSPEnumType): 
            '''Default size of a PCD image when loaded.'''
            Pixels64x96 = 0
            Pixels128x192 = 1
            Pixels256x384 = 2
            Pixels512x768 = 3
            Pixels1024x1536 = 4
            Pixels2048x3072 = 5
            Pixels4096x6144 = 6
            Ask = 7
            def __init__(self):
                self.__name = "ImageSize"
                self.__desc = "Default size of a PCD image when loaded."
                self.__values = [("Pixels64x96", 0, "W=64, H=96"),("Pixels128x192", 1, "W=128, H=192"),("Pixels256x384", 2, "W=256, H=384"),("Pixels512x768", 3, "W=512, H=768"),("Pixels1024x1536", 4, "W=1024, H=1536"),("Pixels2048x3072", 5, "W=2048, H=3072"),("Pixels4096x6144", 6, "W=4096, H=6144"),("Ask", 7, "Ask when loading each file"),]


        class __FileTypesConst(PSPEnumType): 
            '''Type of non-image file.'''
            None = -1
            Tubes = 0
            Patterns = 1
            Textures = 2
            Gradients = 3
            Brushes = 4
            Frames = 5
            Shapes = 6
            StyledLines = 7
            Plugins = 8
            Browsers = 9
            Undo = 10
            RestrictedScripts = 11
            TrustedScripts = 12
            Presets = 13
            Swatches = 14
            SmartBlending = 15
            PythonLibraries = 16
            Cache = 17
            Masks = 18
            Selections = 19
            CYMKProfiles = 20
            PrintTemplates = 21
            Workspaces = 22
            Palettes = 23
            DeformationMaps = 24
            EnvironmentMaps = 25
            BumpMaps = 26
            PythonSourceEditor = 27
            DisplacementMaps = 28
            Categories = 30
            MixerPages = 31
            MonitorProfiles = 32
            def __init__(self):
                self.__name = "FileTypes"
                self.__desc = "Type of non-image file."
                self.__values = [("None", -1, "Special value to indicate that no value was specified."),("Tubes", 0, "Tube files."),("Patterns", 1, "Pattern files."),("Textures", 2, "Texture files."),("Gradients", 3, "Gradient files."),("Brushes", 4, "Brush files."),("Frames", 5, "Frame files."),("Shapes", 6, "Shape files."),("StyledLines", 7, "Styled line files."),("Plugins", 8, "Plugin files."),("Browsers", 9, "Browser files."),("Undo", 10, "Temporary/Undo files."),("RestrictedScripts", 11, "Restricted script files."),("TrustedScripts", 12, "Trusted script files."),("Presets", 13, "Preset files."),("Swatches", 14, "Swatch files."),("SmartBlending", 15, ""),("PythonLibraries", 16, "Python library files."),("Cache", 17, "Cache directory."),("Masks", 18, "Mask files."),("Selections", 19, "Selection files."),("CYMKProfiles", 20, "CMYK profile files."),("PrintTemplates", 21, "Print Template files."),("Workspaces", 22, "Worspace files."),("Palettes", 23, "Palette files."),("DeformationMaps", 24, "Deformation map files."),("EnvironmentMaps", 25, "Environment map files."),("BumpMaps", 26, "Bump map files."),("PythonSourceEditor", 27, "Python source editor."),("DisplacementMaps", 28, "Displacement map files."),("Categories", 30, "Categories database files."),("MixerPages", 31, "Mixer page files."),("MonitorProfiles", 32, "MonitorProfile files"),]


        class __ResolutionUnitsConst(PSPEnumType): 
            '''Default resolution units.'''
            Undefined = 0
            PixelsPerIn = 1
            PixelsPerCM = 2
            def __init__(self):
                self.__name = "ResolutionUnits"
                self.__desc = "Default resolution units."
                self.__values = [("Undefined", 0, "No units given"),("PixelsPerIn", 1, "Pixels per inch"),("PixelsPerCM", 2, "Pixels per centimeter"),]


        class __RulerColorsConst(PSPEnumType): 
            '''Display rulers according to appropriate rule.'''
            BlackOnWhite = 0
            Toolbar = 1
            def __init__(self):
                self.__name = "RulerColors"
                self.__desc = "Display rulers according to appropriate rule."
                self.__values = [("BlackOnWhite", 0, "Display rulers black on white."),("Toolbar", 1, "Display rulers using toolbar colors."),]


        class __UnitsOfMeasureConst(PSPEnumType): 
            '''Display units of measure (ruler or grid).'''
            Pixels = 0
            Inches = 1
            Centimeters = 2
            Millimeters = 3
            Percent = 4
            Undefined = 5
            def __init__(self):
                self.__name = "UnitsOfMeasure"
                self.__desc = "Display units of measure (ruler or grid)."
                self.__values = [("Pixels", 0, "Display units as pixels."),("Inches", 1, "Display units as inches."),("Centimeters", 2, "Display units as centimeters."),("Millimeters", 3, "Display units as millimeters."),("Percent", 4, "Display units as percent."),("Undefined", 5, "No units given."),]


        class __ThumbnailColorsConst(PSPEnumType): 
            '''Thumbnail appearance colors'''
            Windows = 0
            Classic = 1
            def __init__(self):
                self.__name = "ThumbnailColors"
                self.__desc = "Thumbnail appearance colors"
                self.__values = [("Windows", 0, "Use Windows colors"),("Classic", 1, "Use Classic colors"),]


        class __GridSizeConst(PSPEnumType): 
            '''Preview transparency grid size'''
            Tiny = 0
            Small = 1
            Medium = 2
            Large = 3
            def __init__(self):
                self.__name = "GridSize"
                self.__desc = "Preview transparency grid size"
                self.__values = [("Tiny", 0, "Tiny grid size"),("Small", 1, "Small grid size"),("Medium", 2, "Medium grid size"),("Large", 3, "Large grid size"),]


        class __ColorSelectorConst(PSPEnumType): 
            '''Type of color selection tool'''
            Rainbow = 0
            Palette = 1
            def __init__(self):
                self.__name = "ColorSelector"
                self.__desc = "Type of color selection tool"
                self.__values = [("Rainbow", 0, "Rainbow picker"),("Palette", 1, "Document palette"),]


        class __NumericConst(PSPEnumType): 
            '''Color palette numerical display format'''
            Dec = 0
            Hex = 1
            def __init__(self):
                self.__name = "Numeric"
                self.__desc = "Color palette numerical display format"
                self.__values = [("Dec", 0, "Display numbers as decimal."),("Hex", 1, "Display numbers as hexadecimal."),]


        class __ColorFormatConst(PSPEnumType): 
            '''Format of colors displayed in color palette'''
            RGB = 0
            HSL = 1
            def __init__(self):
                self.__name = "ColorFormat"
                self.__desc = "Format of colors displayed in color palette"
                self.__values = [("RGB", 0, "Display colors in RGB format"),("HSL", 1, "Display colors in HSL format"),]


        class __CornerStyleConst(PSPEnumType): 
            '''Type of the blend area used by seamless tiling effect.'''
            Linear = 0
            Curved = 1
            def __init__(self):
                self.__name = "CornerStyle"
                self.__desc = "Type of the blend area used by seamless tiling effect."
                self.__values = [("Linear", 0, "Linear style of the blend area."),("Curved", 1, "Curved style of the blend area."),]


        class __DirectionConst(PSPEnumType): 
            '''Specifies direction in which effect is applied.'''
            Horizontal = 0
            Vertical = 1
            Bidirectional = 2
            def __init__(self):
                self.__name = "Direction"
                self.__desc = "Specifies direction in which effect is applied."
                self.__values = [("Horizontal", 0, "Effect applied only in horizontal directions."),("Vertical", 1, "Effect applied only in vertical directions."),("Bidirectional", 2, "Effect applied in both horizontal and vertical directions."),]


        class __TilingMethodConst(PSPEnumType): 
            '''Defines method to be used to produce an image that can be used as a seamless tile.'''
            Edge = 0
            Corner = 1
            Mirror = 2
            def __init__(self):
                self.__name = "TilingMethod"
                self.__desc = "Defines method to be used to produce an image that can be used as a seamless tile."
                self.__values = [("Edge", 0, "Seamless tile will be produced by blending edges of the image. This method cannot be applied to an image with a selection"),("Corner", 1, "Seamless tile will be produced by blending corners of the image."),("Mirror", 2, "Seamless tile will be produced by blending image with its mirror."),]


        class __JpegFormatConst(PSPEnumType): 
            '''JPEG encoding format - Standard, progressive or lossless'''
            Standard = 0
            Progressive = 1
            Lossless = 2
            def __init__(self):
                self.__name = "JpegFormat"
                self.__desc = "JPEG encoding format - Standard, progressive or lossless"
                self.__values = [("Standard", 0, "Standard Format"),("Progressive", 1, "Progressive Format"),("Lossless", 2, "Lossless Format"),]


        class __SpherizeShapeConst(PSPEnumType): 
            '''Specifies the shape of the effect.'''
            Circle = 0
            Ellipse = 1
            def __init__(self):
                self.__name = "SpherizeShape"
                self.__desc = "Specifies the shape of the effect."
                self.__values = [("Circle", 0, ""),("Ellipse", 1, "Effect is applied in a shape of an ellipse with minor and major diameters equal to the width and height of the image or selection."),]


        class __GradientTypeConst(PSPEnumType): 
            '''Defines the type of gradient; Linear, Radial, Rectangular, or Angular'''
            Linear = 0
            Radial = 1
            Rectangular = 2
            Angular = 3
            def __init__(self):
                self.__name = "GradientType"
                self.__desc = "Defines the type of gradient; Linear, Radial, Rectangular, or Angular"
                self.__values = [("Linear", 0, "Use linear algorithm to create the gradient."),("Radial", 1, "Use radial algorithm to create the gradient."),("Rectangular", 2, "Use rectangle algorithm to create the gradient."),("Angular", 3, "Use angular algorithm to create the gradient."),]


        class __EnterCommandsConst(PSPEnumType): 
            '''Enter, exit, or toggle a function'''
            Enter = 0
            Exit = 1
            Toggle = 2
            def __init__(self):
                self.__name = "EnterCommands"
                self.__desc = "Enter, exit, or toggle a function"
                self.__values = [("Enter", 0, "Enter"),("Exit", 1, "Exit"),("Toggle", 2, "Toggle"),]


        class __ShowCommandsConst(PSPEnumType): 
            '''Show, Hide, or Toggle the item'''
            Show = 0
            Hide = 1
            Toggle = 2
            def __init__(self):
                self.__name = "ShowCommands"
                self.__desc = "Show, Hide, or Toggle the item"
                self.__values = [("Show", 0, "Show the item"),("Hide", 1, "Hide the item"),("Toggle", 2, "Toggle the shown/hidden state of the item"),]


        class __ArithmeticFunctionsConst(PSPEnumType): 
            '''Mathematical functions that can be applied through Arithmetic'''
            Add = 0
            Subtract = 1
            AND = 2
            Average = 3
            Multiply = 4
            Difference = 5
            OR = 6
            Darkest = 7
            Lightest = 8
            XOR = 9
            def __init__(self):
                self.__name = "ArithmeticFunctions"
                self.__desc = "Mathematical functions that can be applied through Arithmetic"
                self.__values = [("Add", 0, "Add 2 images together"),("Subtract", 1, "Subtract 1 image from another"),("AND", 2, "Binary AND"),("Average", 3, "Average of 2 images"),("Multiply", 4, "Multiply 2 images together"),("Difference", 5, "Take the difference between 2 images"),("OR", 6, "Binary OR"),("Darkest", 7, "Take the darkest pixels"),("Lightest", 8, "Take the lightest pixels"),("XOR", 9, "Binary XOR"),]


        class __CaptureActivationConst(PSPEnumType): 
            '''Activate the screenshot with a right mouse click, hot key, or timer'''
            RightMouseClick = 0
            HotKey = 1
            Timer = 2
            PrintScreen = 3
            def __init__(self):
                self.__name = "CaptureActivation"
                self.__desc = "Activate the screenshot with a right mouse click, hot key, or timer"
                self.__values = [("RightMouseClick", 0, "Activate the screenshot with a right mouse click"),("HotKey", 1, "Activate the screenshot with a hot key"),("Timer", 2, "Activate the screenshot with a timer"),("PrintScreen", 3, "Activate the screenshot with a timer"),]


        class __CaptureTypeConst(PSPEnumType): 
            '''Describes the kind of screenshot to be done.'''
            Smart = 0
            Area = 1
            FullScreen = 2
            Window = 3
            Object = 4
            ClientArea = 5
            def __init__(self):
                self.__name = "CaptureType"
                self.__desc = "Describes the kind of screenshot to be done."
                self.__values = [("Smart", 0, "Capture an object"),("Area", 1, "Capture a user defined area"),("FullScreen", 2, "Capture the full screen"),("Window", 3, "Capture a window"),("Object", 4, "Capture an object"),("ClientArea", 5, "Capture a client area"),]


        class __PresetUnitTypeConst(PSPEnumType): 
            '''Describes the kind of size of unit typee'''
            Pixels = 0
            Ratio = 1
            def __init__(self):
                self.__name = "PresetUnitType"
                self.__desc = "Describes the kind of size of unit typee"
                self.__values = [("Pixels", 0, "Size by pixels"),("Ratio", 1, "Size by ratio"),]


        class __RepeatTypeConst(PSPEnumType): 
            '''Defines a gradient paintstyle repeat type; Pad, Reflect, or Repeat'''
            Pad = 0
            Reflect = 1
            Repeat = 2
            def __init__(self):
                self.__name = "RepeatType"
                self.__desc = "Defines a gradient paintstyle repeat type; Pad, Reflect, or Repeat"
                self.__values = [("Pad", 0, "Use the terminal colors of the gradient to fill the remainder of the target region."),("Reflect", 1, "Reflect the gradient pattern start-to-end, end-to-start, start-to-end, etc. continuously until the target region is filled."),("Repeat", 2, "Repeat the gradient pattern start-to-end, start-to-end, start-to-end, etc. continuously until the target region is filled."),]


        class __ContrastStrengthConst(PSPEnumType): 
            '''Specifies strength of the effect.'''
            Normal = 0
            Mild = 1
            def __init__(self):
                self.__name = "ContrastStrength"
                self.__desc = "Specifies strength of the effect."
                self.__values = [("Normal", 0, "Normal strength."),("Mild", 1, "Mild strength."),]


        class __SaturationStrengthConst(PSPEnumType): 
            '''Specifies strength of the effect.'''
            Weak = 0
            Normal = 1
            Strong = 2
            def __init__(self):
                self.__name = "SaturationStrength"
                self.__desc = "Specifies strength of the effect."
                self.__values = [("Weak", 0, "Weak strength."),("Normal", 1, "Normal strength."),("Strong", 2, "Strong."),]


        class __ScratchRemovalStrengthConst(PSPEnumType): 
            '''Specifies strength of the effect.'''
            Mild = 0
            Normal = 1
            Aggressive = 2
            def __init__(self):
                self.__name = "ScratchRemovalStrength"
                self.__desc = "Specifies strength of the effect."
                self.__values = [("Mild", 0, "Mild strength."),("Normal", 1, "Normal strength."),("Aggressive", 2, "Aggressive."),]


        class __JPEGStrengthConst(PSPEnumType): 
            '''Specifies strength of the effect.'''
            Low = 0
            Normal = 1
            High = 2
            Maximum = 3
            def __init__(self):
                self.__name = "JPEGStrength"
                self.__desc = "Specifies strength of the effect."
                self.__values = [("Low", 0, "Low strength."),("Normal", 1, "Normal strength."),("High", 2, "High strength."),("Maximum", 3, "Maximum strength."),]


        class __AppearanceConst(PSPEnumType): 
            '''Defines the appearance of the image after the effect has been applied.'''
            Flat = 0
            Natural = 1
            Bold = 2
            def __init__(self):
                self.__name = "Appearance"
                self.__desc = "Defines the appearance of the image after the effect has been applied."
                self.__values = [("Flat", 0, "Image will appear flatter."),("Natural", 1, "Image features will appear more natural."),("Bold", 2, "Image features will look bolder."),]


        class __ContrastBiasConst(PSPEnumType): 
            '''Bias value for contrast enhancement'''
            Lighter = 0
            Neutral = 1
            Darker = 2
            def __init__(self):
                self.__name = "ContrastBias"
                self.__desc = "Bias value for contrast enhancement"
                self.__values = [("Lighter", 0, "Effect will produce lighter image."),("Neutral", 1, "Effect will produce normal/neutral image."),("Darker", 2, "Effect will produce darker image."),]


        class __SaturationBiasConst(PSPEnumType): 
            '''Bias value for saturation enhancement'''
            LessColorful = 0
            Normal = 1
            MoreColorful = 2
            def __init__(self):
                self.__name = "SaturationBias"
                self.__desc = "Bias value for saturation enhancement"
                self.__values = [("LessColorful", 0, "Effect will produce less colorful image."),("Normal", 1, "Effect will produce normal/neutral image."),("MoreColorful", 2, "Effect will produce more colorful image."),]


        class __EdgeModeConst(PSPEnumType): 
            '''Edge mode defines the method to fill pixels that are not mapped by the deformation.'''
            Wrap = 0
            Repeat = 1
            Background = 2
            Transparent = 3
            def __init__(self):
                self.__name = "EdgeMode"
                self.__desc = "Edge mode defines the method to fill pixels that are not mapped by the deformation."
                self.__values = [("Wrap", 0, "Uses pixels on other side of image to fill unmapped pixels."),("Repeat", 1, "Repeats pixels in fill unmapped pixels."),("Background", 2, "Uses background pixels in fill unmapped pixels."),("Transparent", 3, "Sets unmapped pixels to transparent."),]


        class __BooleanConst(PSPEnumType): 
            '''Defines True and False to be one and zero'''
            false = 0
            true = 1
            def __init__(self):
                self.__name = "Boolean"
                self.__desc = "Defines True and False to be one and zero"
                self.__values = [("false", 0, "Boolean value is False"),("true", 1, "Boolean value is True"),]


        class __ExecutionModeConst(PSPEnumType): 
            '''Execution mode defines how the command will run; e.g., interactive or silent.'''
            Default = 0
            Interactive = 1
            Silent = 2
            EditOnce = 3
            EditOnly = 4
            SilentFix = 5
            def __init__(self):
                self.__name = "ExecutionMode"
                self.__desc = "Execution mode defines how the command will run; e.g., interactive or silent."
                self.__values = [("Default", 0, "Defer to the parent execution mode."),("Interactive", 1, "Display dialog to edit parameters, then execute command."),("Silent", 2, "Execute command without displaying dialog."),("EditOnce", 3, "Display dialog on first execution, but subsequent executions are silent."),("EditOnly", 4, "Display the dialog, but do not execute the command."),("SilentFix", 5, "Execute command without displaying dialog."),]


        class __DisplacementMethodConst(PSPEnumType): 
            '''Displacement method'''
            Offset2D = 0
            Surface3D = 1
            def __init__(self):
                self.__name = "DisplacementMethod"
                self.__desc = "Displacement method"
                self.__values = [("Offset2D", 0, "Interpret displacement map as matrix of offsets"),("Surface3D", 1, "Interpret displacement map as 3D surface"),]


        class __EdgeFeatherConst(PSPEnumType): 
            '''EdgeFeather'''
            Rectangular = 0
            Circular = 1
            Jagged = 2
            def __init__(self):
                self.__name = "EdgeFeather"
                self.__desc = "EdgeFeather"
                self.__values = [("Rectangular", 0, ""),("Circular", 1, ""),("Jagged", 2, ""),]


        class __TimeMachineConst(PSPEnumType): 
            '''TimeMachine'''
            Daguerreotype = 0
            Albumen = 1
            Cyanotype = 2
            Platinotype = 3
            EarlyColor = 4
            FadedColor = 5
            Brownie = 6
            CrossProcess = 7
            def __init__(self):
                self.__name = "TimeMachine"
                self.__desc = "TimeMachine"
                self.__values = [("Daguerreotype", 0, ""),("Albumen", 1, ""),("Cyanotype", 2, ""),("Platinotype", 3, ""),("EarlyColor", 4, ""),("FadedColor", 5, ""),("Brownie", 6, ""),("CrossProcess", 7, ""),]


        def __init__(self, constants):
            self.__constants = constants
            self.SeamCarvingAction = self.__SeamCarvingActionConst() 
            self.HDPVariant = self.__HDPVariantConst() 
            self.PhotoLookEffect = self.__PhotoLookEffectConst() 
            self.keImageQuality = self.__keImageQualityConst() 
            self.OptimizedSize = self.__OptimizedSizeConst() 
            self.MakeoverMode = self.__MakeoverModeConst() 
            self.PolarDirection = self.__PolarDirectionConst() 
            self.MaterialStyle = self.__MaterialStyleConst() 
            self.EyeColor = self.__EyeColorConst() 
            self.DeformationMapFormat = self.__DeformationMapFormatConst() 
            self.JascFileFormats = self.__JascFileFormatsConst() 
            self.Event = self.__EventConst() 
            self.AutoShowPalettes = self.__AutoShowPalettesConst() 
            self.BlackAndWhiteFilterColor = self.__BlackAndWhiteFilterColorConst() 
            self.CheckpointTransientData = self.__CheckpointTransientDataConst() 
            self.Gradient = self.__GradientConst() 
            self.PictureFrameTarget = self.__PictureFrameTargetConst() 
            self.CheckpointDataFormat = self.__CheckpointDataFormatConst() 
            self.SharpenMode = self.__SharpenModeConst() 
            self.WhiteBalance = self.__WhiteBalanceConst() 
            self.MouseButton = self.__MouseButtonConst() 
            self.ImageInfoPropertySheet = self.__ImageInfoPropertySheetConst() 
            self.MixerSampleMode = self.__MixerSampleModeConst() 
            self.MixerActiveTool = self.__MixerActiveToolConst() 
            self.MixerMode = self.__MixerModeConst() 
            self.ResourceListView = self.__ResourceListViewConst() 
            self.ArtMediaPencilStyle = self.__ArtMediaPencilStyleConst() 
            self.ArtMediaBrushCleaning = self.__ArtMediaBrushCleaningConst() 
            self.ArtMediaBrushShape = self.__ArtMediaBrushShapeConst() 
            self.ArtMediaBrushRotation = self.__ArtMediaBrushRotationConst() 
            self.AntialiasEx = self.__AntialiasExConst() 
            self.NewLayerType = self.__NewLayerTypeConst() 
            self.TextFlow = self.__TextFlowConst() 
            self.InitializeTo = self.__InitializeToConst() 
            self.PathEntryType = self.__PathEntryTypeConst() 
            self.NoiseType = self.__NoiseTypeConst() 
            self.PointRelativeBasis = self.__PointRelativeBasisConst() 
            self.BatchMode = self.__BatchModeConst() 
            self.PaletteTransparency = self.__PaletteTransparencyConst() 
            self.PaletteMethod = self.__PaletteMethodConst() 
            self.ErrorDiffusion = self.__ErrorDiffusionConst() 
            self.PaletteComponent = self.__PaletteComponentConst() 
            self.ReductionMethod = self.__ReductionMethodConst() 
            self.TonalRange = self.__TonalRangeConst() 
            self.TransformType = self.__TransformTypeConst() 
            self.LensMapType = self.__LensMapTypeConst() 
            self.DimensionType = self.__DimensionTypeConst() 
            self.Colordepth = self.__ColordepthConst() 
            self.ColorCorrection = self.__ColorCorrectionConst() 
            self.ParamInfo = self.__ParamInfoConst() 
            self.PaletteFormat = self.__PaletteFormatConst() 
            self.MatchMode = self.__MatchModeConst() 
            self.HistogramEditMode = self.__HistogramEditModeConst() 
            self.GridColorScheme = self.__GridColorSchemeConst() 
            self.AppOutputFiltering = self.__AppOutputFilteringConst() 
            self.SelectionType = self.__SelectionTypeConst() 
            self.MapShapeType = self.__MapShapeTypeConst() 
            self.WebFileType = self.__WebFileTypeConst() 
            self.WebFrameTarget = self.__WebFrameTargetConst() 
            self.AutoActionMode = self.__AutoActionModeConst() 
            self.FileFormat = self.__FileFormatConst() 
            self.ObjectPlacement = self.__ObjectPlacementConst() 
            self.MeshWarpingSymmetricMode = self.__MeshWarpingSymmetricModeConst() 
            self.GeneralPreferencesTabs = self.__GeneralPreferencesTabsConst() 
            self.CropUnits = self.__CropUnitsConst() 
            self.CropMode = self.__CropModeConst() 
            self.TubeSelectionMode = self.__TubeSelectionModeConst() 
            self.TubePlacementMode = self.__TubePlacementModeConst() 
            self.WarpingBrushFinalApplyQuality = self.__WarpingBrushFinalApplyQualityConst() 
            self.WarpingBrushDraftQuality = self.__WarpingBrushDraftQualityConst() 
            self.WarpingBrushEdgeMode = self.__WarpingBrushEdgeModeConst() 
            self.LayerType = self.__LayerTypeConst() 
            self.Jp2Variant = self.__Jp2VariantConst() 
            self.AntialiasType = self.__AntialiasTypeConst() 
            self.Jp2Quality = self.__Jp2QualityConst() 
            self.ChromaSubSampling = self.__ChromaSubSamplingConst() 
            self.ClipboardExit = self.__ClipboardExitConst() 
            self.OnOff = self.__OnOffConst() 
            self.PromptState = self.__PromptStateConst() 
            self.SaveAllNoneList = self.__SaveAllNoneListConst() 
            self.HMSAdjustmentMethod = self.__HMSAdjustmentMethodConst() 
            self.PictureTubeSelectionMode = self.__PictureTubeSelectionModeConst() 
            self.BackgroundEraserSamplingMode = self.__BackgroundEraserSamplingModeConst() 
            self.BackgroundEraserLimits = self.__BackgroundEraserLimitsConst() 
            self.RetouchChangeToTargetModes = self.__RetouchChangeToTargetModesConst() 
            self.PlacementMode = self.__PlacementModeConst() 
            self.RetouchDirection = self.__RetouchDirectionConst() 
            self.RetouchLightenDarkenModes = self.__RetouchLightenDarkenModesConst() 
            self.RedEyeMethod = self.__RedEyeMethodConst() 
            self.SelectionModifyType = self.__SelectionModifyTypeConst() 
            self.MaskFill = self.__MaskFillConst() 
            self.MaskLoadOrientation = self.__MaskLoadOrientationConst() 
            self.CreateAlphaFrom = self.__CreateAlphaFromConst() 
            self.SelectionShape = self.__SelectionShapeConst() 
            self.SelectionStyle = self.__SelectionStyleConst() 
            self.LayerOrSelection = self.__LayerOrSelectionConst() 
            self.Orientation = self.__OrientationConst() 
            self.ViewMaskOverlay = self.__ViewMaskOverlayConst() 
            self.ObjectSelection = self.__ObjectSelectionConst() 
            self.MaterialRef = self.__MaterialRefConst() 
            self.PixelFormat = self.__PixelFormatConst() 
            self.PrintPagePosition = self.__PrintPagePositionConst() 
            self.PrintRange = self.__PrintRangeConst() 
            self.PathEntryInterpretation = self.__PathEntryInterpretationConst() 
            self.VarianceMethod = self.__VarianceMethodConst() 
            self.JointStyle = self.__JointStyleConst() 
            self.CreateAs = self.__CreateAsConst() 
            self.FontSizeUnits = self.__FontSizeUnitsConst() 
            self.TextType = self.__TextTypeConst() 
            self.Justify = self.__JustifyConst() 
            self.ColorRangeAction = self.__ColorRangeActionConst() 
            self.BubbleCreateMethod = self.__BubbleCreateMethodConst() 
            self.FeatheringType = self.__FeatheringTypeConst() 
            self.RemoveSpecksHolesType = self.__RemoveSpecksHolesTypeConst() 
            self.WarpingBrushMode = self.__WarpingBrushModeConst() 
            self.BubbleMapType = self.__BubbleMapTypeConst() 
            self.CountType = self.__CountTypeConst() 
            self.LensFrameShape = self.__LensFrameShapeConst() 
            self.LensFrameMaterial = self.__LensFrameMaterialConst() 
            self.LensShape = self.__LensShapeConst() 
            self.RotateMode = self.__RotateModeConst() 
            self.BordersType = self.__BordersTypeConst() 
            self.TileShape = self.__TileShapeConst() 
            self.CreateMaskFrom = self.__CreateMaskFromConst() 
            self.WpgVersion = self.__WpgVersionConst() 
            self.TgaColors = self.__TgaColorsConst() 
            self.SctChannels = self.__SctChannelsConst() 
            self.RleFormat = self.__RleFormatConst() 
            self.PspVersion = self.__PspVersionConst() 
            self.PspCompression = self.__PspCompressionConst() 
            self.PcxVersion = self.__PcxVersionConst() 
            self.DataEncoding = self.__DataEncodingConst() 
            self.GifVersion = self.__GifVersionConst() 
            self.BmpFormat = self.__BmpFormatConst() 
            self.VerticalType = self.__VerticalTypeConst() 
            self.HorizontalType = self.__HorizontalTypeConst() 
            self.MsgButtons = self.__MsgButtonsConst() 
            self.MsgIcons = self.__MsgIconsConst() 
            self.BrushShape = self.__BrushShapeConst() 
            self.SelectionOperation = self.__SelectionOperationConst() 
            self.FreehandSelectionType = self.__FreehandSelectionTypeConst() 
            self.DistortionType = self.__DistortionTypeConst() 
            self.ResampleType = self.__ResampleTypeConst() 
            self.TransparencyType = self.__TransparencyTypeConst() 
            self.ImageType = self.__ImageTypeConst() 
            self.Version = self.__VersionConst() 
            self.SubFormat = self.__SubFormatConst() 
            self.ColorSelection = self.__ColorSelectionConst() 
            self.PartialTransparency = self.__PartialTransparencyConst() 
            self.Transparency = self.__TransparencyConst() 
            self.ColorScheme = self.__ColorSchemeConst() 
            self.HalftonePattern = self.__HalftonePatternConst() 
            self.BlendMode = self.__BlendModeConst() 
            self.PageSize = self.__PageSizeConst() 
            self.DisplacementMapType = self.__DisplacementMapTypeConst() 
            self.DisplacementLayout = self.__DisplacementLayoutConst() 
            self.RadialBlurType = self.__RadialBlurTypeConst() 
            self.CAMGEngineType = self.__CAMGEngineTypeConst() 
            self.TiffCompression = self.__TiffCompressionConst() 
            self.ColorChannels = self.__ColorChannelsConst() 
            self.JpegEncoding = self.__JpegEncodingConst() 
            self.ColorOrder = self.__ColorOrderConst() 
            self.ImageMode = self.__ImageModeConst() 
            self.ImageSize = self.__ImageSizeConst() 
            self.FileTypes = self.__FileTypesConst() 
            self.ResolutionUnits = self.__ResolutionUnitsConst() 
            self.RulerColors = self.__RulerColorsConst() 
            self.UnitsOfMeasure = self.__UnitsOfMeasureConst() 
            self.ThumbnailColors = self.__ThumbnailColorsConst() 
            self.GridSize = self.__GridSizeConst() 
            self.ColorSelector = self.__ColorSelectorConst() 
            self.Numeric = self.__NumericConst() 
            self.ColorFormat = self.__ColorFormatConst() 
            self.CornerStyle = self.__CornerStyleConst() 
            self.Direction = self.__DirectionConst() 
            self.TilingMethod = self.__TilingMethodConst() 
            self.JpegFormat = self.__JpegFormatConst() 
            self.SpherizeShape = self.__SpherizeShapeConst() 
            self.GradientType = self.__GradientTypeConst() 
            self.EnterCommands = self.__EnterCommandsConst() 
            self.ShowCommands = self.__ShowCommandsConst() 
            self.ArithmeticFunctions = self.__ArithmeticFunctionsConst() 
            self.CaptureActivation = self.__CaptureActivationConst() 
            self.CaptureType = self.__CaptureTypeConst() 
            self.PresetUnitType = self.__PresetUnitTypeConst() 
            self.RepeatType = self.__RepeatTypeConst() 
            self.ContrastStrength = self.__ContrastStrengthConst() 
            self.SaturationStrength = self.__SaturationStrengthConst() 
            self.ScratchRemovalStrength = self.__ScratchRemovalStrengthConst() 
            self.JPEGStrength = self.__JPEGStrengthConst() 
            self.Appearance = self.__AppearanceConst() 
            self.ContrastBias = self.__ContrastBiasConst() 
            self.SaturationBias = self.__SaturationBiasConst() 
            self.EdgeMode = self.__EdgeModeConst() 
            self.Boolean = self.__BooleanConst() 
            self.ExecutionMode = self.__ExecutionModeConst() 
            self.DisplacementMethod = self.__DisplacementMethodConst() 
            self.EdgeFeather = self.__EdgeFeatherConst() 
            self.TimeMachine = self.__TimeMachineConst() 
        def All(self):
            return self.__constants
        def __getattr__(self, key):
            for x in self.__constants:
                if x.Name() == key:
                    return x
App = APP()
