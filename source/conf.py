# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
# 项目名
project = 'A Sphinx Book Template'
# 版权，著作权
copyright = '2024, leehaonan'
# 作者
author = 'leehaonan'

# The short X.Y version. 主要项目版本，用作 |version| .
version = 'alpha'
# The full version, including alpha/beta/rc tags. 完整的项目版本，用作 |release|
release = 'alpha'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d, %H:%M:%S"

# The encoding of source files.
# 建议的编码和默认值是 'utf-8-sig' .
source_encoding = 'utf-8-sig'

# The master toctree document.
# “主控”文档的文档名称，即包含根目录的文档 toctree 指令。
# 在 2.0 版更改: 默认值更改为 'index' 从 'contents' .
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 在这里以字符串的形式添加任何Sphinx扩展模块名。
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
]
# "sphinx.ext.todo" : 对TODO项的支持
# "sphinx.ext.intersphinx" :链接到其他项目的文档
# "sphinx.ext.autosectionlabel" : label 标签自动选中确保唯一性,并允许引用节使用其标题,同时自动为标题创建label
# 'myst_parser' : myst 解析器, 默认情况下，myst_parser 会解析 markdown(.md) ,而 .rst 文件会被 Sphinx 原生解析器 restructureText 解析。
# "sphinx_design" : 用于设计美观、视图大小的响应式 Web 组件。
# "sphinx_copybutton": 代码块复制按钮扩展

# Make sure the target is unique (sphinx.ext.autosectionlabel 插件的配置)
autosectionlabel_prefix_document = True

# MyST Markdown 扩展语法
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "smartquotes", "replacements",
    "linkify",
    "html_image",
    "substitution",
    "dollarmath", "amsmath",
]
# 如果为false,只有包含方案（例如http）的链接才会被识别为外部链接
myst_linkify_fuzzy_links = False
# substitution 的扩展的全局替换，作用于 .md
myst_substitutions = {}
# default is ['{', '}']，替换指令分隔符，不建议更改
# myst_sub_delimiters = ["|", "|"]

# 数学公式语法 $ （dollar math） 设置
myst_dmath_allow_labels = True
myst_dmath_double_inline = True
# myst_dmath_allow_space = False, will cause inline math to only be parsed if there are no initial / final spaces, e.g. $a$ but not $ a$ or $a $.
# myst_dmath_allow_digits = False, will cause inline math to only be parsed if there are no initial / final digits, e.g. $a$ but not 1$a$ or $a$2.

# -- global replace order configuration are as follows---
# 全局字符串替换指令
# 需要注意的是，全局加入替换的功能要谨慎使用，要酌情使用；因为在这里添加后会影响到项目所有的 rst 文件（在所有 rst 文件中添加定义的替换指令）
# 一串 reStructuredText，它将包含在每个读取的源文件的末尾。 这是一个可以添加应该在每个文件中可用的替换的地方
rst_prolog = """
.. |15| raw:: html
      
      <hr width='15%'>

.. |30| raw:: html
      
      <hr width='30%'>
      
.. |50| raw:: html
      
      <hr width='50%'>

.. |75| raw:: html
      
      <hr width='75%'>

"""

# 图片编号功能
# -- numfig configuration are as follows---
# 表格和代码块如果有标题则会自动编号
numfig = True
# -- numfig_secnum_depth configuration are as follows---
# 如果设置为“0”，则数字，表格和代码块从“1”开始连续编号。
# 如果“1”(默认)，数字将是“x.1”。“x.2”，… 与“x”的节号(顶级切片;没有“x”如果没有部分)。只有当通过 toctree 指令的“:numbered:”选项激活了段号时，这才自然适用。
# 如果“2”，表示数字将是“x.y.1”，“x.y.2”，…如果位于子区域(但仍然是 x.1 ，x.2 ，… 如果直接位于一个部分和 1 ，2 ， … 如果不在任何顶级部分。)
numfig_secnum_depth = 2
# -- numfig_format configuration are as follows---
# 一个字典将“‘figure’”，“‘table’”，“‘code-block’”和“‘section’”映射到用于图号格式的字符串。作为一个特殊字符，“%s”将被替换为图号。
# 默认是使用“‘Fig.%s’”为“‘figure’”, “‘Table%s’”为“‘table’”，“‘Listing%s’”为“‘code-block’”和“‘Section’”为 “‘section’”。
numfig_format = {'code-block': '代码块 %s', }
# -- html_codeblock_linenos_style configuration are as follows---
# 代码块的行号样式
html_codeblock_linenos_style = 'table'
# html_codeblock_linenos_style = 'inline'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# 主题配置
html_theme = "sphinx_book_theme"
# 以下为 sphinx_book_theme 的主题配置/定制（sphinx_book_theme）
html_theme_options = {

    # ----------------主题内容中导航栏的功能按钮配置--------
    # 添加存储库链接
    "repository_url": "https://github.com/LHNCreate/BuggyAutoSAR",
    # 添加按钮以链接到存储库
    "use_repository_button": True,
    # 要添加按钮以打开有关当前页面的问题
    "use_issues_button": True,
    # 添加一个按钮来建议编辑
    "use_edit_page_button": True,
    # 在导航栏添加一个按钮来切换全屏的模式。
    "use_fullscreen_button": True,  # 默认 `True`
    # 默认情况下，编辑按钮将指向master分支，但如果您想更改此设置，请使用以下配置
    "repository_branch": "main",
    # 默认情况下，编辑按钮将指向存储库的根目录；而我们 sphinx项目的 doc文件其实是在 source 文件夹下的，包括 conf.py 和 index(.rst) 主目录
    "path_to_docs": "source",
    # 您可以添加 use_download_button 按钮，允许用户以多种格式下载当前查看的页面
    "use_download_button": True,

    # --------------------------右侧辅助栏配置---------
    # 重命名右侧边栏页内目录名，标题的默认值为Contents。
    "toc_title": "导航",
    # -- 在导航栏中显示子目录，向下到这里列出的深度。 ----
    "show_toc_level": 2,

    # --------------------------左侧边栏配置--------------
    # -- 只显示标识，不显示 `html_title`，如果它存在的话。-----
    "logo_only": True,
    # 控制左侧边栏列表的深度展开,默认值为1，它仅显示文档的顶级部分
    "show_navbar_depth": 1,
    # 自定义侧边栏页脚,默认为 Theme by the Executable Book Project
    # "extra_navbar": "<p>Your HTML</p>",
    "home_page_in_toc": False,  # 是否将主页放在导航栏（顶部）

    # ------------------------- 单页模式 -----------------
    # 如果您的文档只有一个页面，并且您不需要左侧导航栏，那么您可以 使用以下配置将其配置sphinx-book-theme 为以单页模式运行
    # "single_page": True,

    # -- 在每个页面的页脚添加额外的 HTML。---
    # "extra_footer": '',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# 添加你自己的 CSS 规则
html_static_path = ['_static']
html_css_files = ["custom.css"]


# 自定义徽标、和网站图标
# 自定义徽标、和网站图标
html_logo = "./_static/notebook-badge.svg"
html_favicon = "./_static/notebook-badge.svg"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
