import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-sale-reporting",
    description="Meta package for oca-sale-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-sale_comment_template',
        'odoo13-addon-sale_layout_category_hide_detail',
        'odoo13-addon-sale_order_line_position',
        'odoo13-addon-sale_order_report_product_image',
        'odoo13-addon-sale_report_country_state',
        'odoo13-addon-sale_report_delivered_subtotal',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
