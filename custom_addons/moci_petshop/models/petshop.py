from odoo import models, fields, api

class MociPet(models.Model):
    _name = 'moci.pet'
    _description = 'Data Hewan Peliharaan'

    name = fields.Char(string='Nama Hewan', required=True)
    species = fields.Selection([
        ('cat', 'Kucing'),
        ('dog', 'Anjing'),
        ('other', 'Lainnya')
    ], string='Spesies', default='cat', required=True)
    breed = fields.Char(string='Ras/Jenis')
    owner_id = fields.Many2one('res.partner', string='Pemilik', required=True)
    notes = fields.Text(string='Catatan Medis/Perawatan')

class MociGrooming(models.Model):
    _name = 'moci.grooming'
    _description = 'Layanan Grooming'

    name = fields.Char(string='ID Referensi', required=True, copy=False, readonly=True, default='New')
    pet_id = fields.Many2one('moci.pet', string='Hewan Peliharaan', required=True)
    owner_id = fields.Many2one(related='pet_id.owner_id', string='Pemilik', readonly=True)
    service_date = fields.Datetime(string='Tanggal Layanan', default=fields.Datetime.now)
    service_type = fields.Selection([
        ('basic', 'Basic Grooming'),
        ('medical', 'Medical Grooming (Kutu/Jamur)'),
        ('full', 'Full Grooming')
    ], string='Jenis Layanan', required=True)
    
    # Tambahan 3 field baru
    price = fields.Float(string='Harga Layanan', required=True, default=0.0)
    sale_order_id = fields.Many2one('sale.order', string='Sales Order / Nota', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('process', 'Sedang Diproses'),
        ('done', 'Selesai')
    ], string='Status', default='draft')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('moci.grooming') or 'New'
        return super(MociGrooming, self).create(vals_list)

    # Fungsi baru untuk membuat otomatisasi Sales Order
    def action_create_sales_order(self):
        for record in self:
            # 1. Cari produk 'Layanan Petshop' di database
            product = self.env['product.product'].search([('name', '=', 'Layanan Petshop')], limit=1)
            
            # Jika belum ada, buat otomatis sebagai tipe 'Jasa/Service'
            if not product:
                product = self.env['product.product'].create({
                    'name': 'Layanan Petshop',
                    'type': 'service',
                    'list_price': 0.0,
                })

            # 2. Buat Header Dokumen Sales Order
            sale_order = self.env['sale.order'].create({
                'partner_id': record.owner_id.id,
                'origin': record.name, 
            })
            
            # 3. Buat Baris Item Layanan di Sales Order (Tambahkan product_id)
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': product.id,  # <-- Ini field yang diwajibkan Odoo
                'name': f'Layanan {record.service_type} untuk {record.pet_id.name}',
                'product_uom_qty': 1,
                'price_unit': record.price,
            })
            
            # 4. Tautkan SO ke dokumen Grooming ini dan ubah status jadi Selesai
            record.sale_order_id = sale_order.id
            record.state = 'done'