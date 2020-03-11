# 登录账户设置
USER = 'admin'
PASSWORD = 'admin'

DOMAIN = 'http://wppy.com'  #在这里修改url
PAGE_LINK = DOMAIN + '/wp-admin/post-new.php?post_type=page'
# 登录url
LOGIN = DOMAIN + '/wp-admin' 

# 打开的文件夹
FOLDER = ''

# 需要创建的文件夹
AIM_FOLDER = ''


# header的内容替换
file_head = """
<head>
		<?php //wp_head(); ?>
	<meta charset="utf-8">
	<meta http-equiv="Content-Type" content="text/html">
	<title>
		<?php if (function_exists('is_tag') && is_tag()) {
			single_tag_title('Tag Archive for "');
			echo '" - ';
		} elseif (is_archive()) {
			wp_title('');
			echo ' Archive - ';
		} elseif (is_search()) {
			echo 'Search for "' . wp_specialchars($s) . '" - ';
		} elseif (!(is_404()) && (is_single()) || (is_page())) {
			wp_title('');
			echo ' - ';
		} elseif (is_404()) {
			echo 'Not Found - ';
		}
		if (is_home()) {
			bloginfo('name');
			echo ' - ';
			bloginfo('description');
		} else {
			bloginfo('name');
		}
		if ($paged > 1) {
			echo ' - page ' . $paged;
		} ?>
	</title>

	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta content="yes" name="apple-mobile-web-app-capable">
	<meta content="yes" name="apple-touch-fullscreen">
	<meta content="<?php echo get_setting('keywords') ?>" name="keywords">
	<meta content="<?php echo get_setting('description') ?>" name="description">
	<meta content="initial-scale=1.0, minimum-scale=1.0, maximum-scale=2.0, user-scalable=no, width=device-width" name="viewport">
	<link rel="icon" href="<?php echo get_site_icon_url() ?>" type="image/x-icon">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/fontawesome/css/font-awesome.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/global.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/widget.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/variousComponents.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/images.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/628/css/theme.css">
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/628/css/color_0.css">
	<script src="<?php echo ROOT ?>/static/js/jquery.min.js"></script>
	<!--[if !IE]><!-->
	<script src="<?php echo ROOT ?>/static/js/base.js"></script>
	<!--<![endif]-->
	<!--[if gte IE 9]>
	<script src="<?php echo ROOT ?>/static/js/base.js"></script>
	<![endif]-->
	<!--[if lt IE 9]>
	<link rel="stylesheet" href="http://ievoqc.r11.35.com/<?php echo ROOT ?>/static/628/css/fontawesome/css/font-awesome-ie7.min.css">
	<script src="<?php echo ROOT ?>/static/js/selectivizr.js"></script>
	<script src="html5shiv/3.7.2/html5shiv.min.js"></script>
	<script src="respond.js/1.4.2/respond.min.js"></script>
	<script src="modernizr/2.8.2/modernizr.min.js"></script>
	<![endif]-->
	<link href="<?php echo ROOT ?>/static/js/plugins/lightbox/css/lightbox.min.css" rel="stylesheet">
	<script src="<?php echo ROOT ?>/static/js/jquery.SuperSlide.js"></script>
	<script src="<?php echo ROOT ?>/static/js/common.js"></script>
	<script src="<?php echo ROOT ?>/static/628/js/theme.js"></script>
	<!-- feib -->
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/plugins/layer/layer.js"></script>
	<!-- plugins -->
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/plugins/jQuery.formsValidation.js"></script>
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/plugins/jQuery.nodeCommon.js"></script>
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/plugins/extend.js"></script>
	<link rel="stylesheet" href="<?php echo ROOT ?>/static/css/animate.min.css">
	<script src="<?php echo ROOT ?>/static/js/animate.min.js"></script>
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/components.js"></script>
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/jquery.menu_style.js"></script>
	<script type="text/javascript" src="<?php echo ROOT ?>/static/js/jquery.init.js"></script>
	<script type="text/javascript">
		$(function() {
			dataAnimate();
			(function($, lanno) {
				if (lanno === "" || lanno === "default") {
					return '';
				}
				$(".w-languege").each(function() {
					$(this).find("a").each(function() {
						if ($(this).data("lanno") === lanno) {
							$(this).addClass("cur");
						} else {
							if ($(this).hasClass("cur")) {
								$(this).removeClass("cur");
							}
						}
					});
				});
			})(jQuery, "cn");
		});
	</script>
	<script>
		/*兼容wordpress导航结构*/
		$(function() {
			$('.menu-header_menu-container').addClass('w-nav-in')
			$('.menu-header_menu-container > ul').append('<div class="nav_moveBox"></div>')
			$('.menu-header_menu-container > ul').addClass('nav_inner clearfix').attr('id', 'g-web-ul-menu')
			$('.w-nav-in li[class*=current-]').addClass("active")

			$('#g-web-ul-menu > li > a:first-child')
				.append('<i class="fa fa-plus"></i>')
				.wrap('<div class="li-parent-div li-parentOne-div"></div>')

			$('.li-parent-div.li-parentOne-div').after('<i class="nav_simpline_cur"></i>')

			$('.sub-menu')
				.prepend('<div class="back-div"><i class="fa fa-angle-left"></i><span>返回</span></div>')
				.wrap('<div class="submenu"></div>')
		})
	</script>
</head>
"""

