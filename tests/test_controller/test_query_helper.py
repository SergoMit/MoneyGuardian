import bookkeeper.controller.query_helper as qh


def test_get_residual(mocker):
    mocker.patch('bookkeeper.controller.query_helper.get_budget', return_value=[500, 1000, 2000])
    mocker.patch('bookkeeper.controller.query_helper.get_day_total', return_value=300)
    assert qh.get_day_residual() == 200

def test_get_week_residual(mocker):
    mocker.patch('bookkeeper.controller.query_helper.get_budget', return_value=[500, 1000, 2000])
    mocker.patch('bookkeeper.controller.query_helper.get_week_total', return_value=700)
    assert qh.get_week_residual() == 300
    
def test_get_month_residual(mocker):
    mocker.patch('bookkeeper.controller.query_helper.get_budget', return_value=[500, 1000, 2000])
    mocker.patch('bookkeeper.controller.query_helper.get_month_total', return_value=1500)
    assert qh.get_month_residual() == 500
