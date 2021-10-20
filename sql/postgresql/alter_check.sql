-- adds a CHECK condition to the target column 
-- so that the targetcolumn only accepts the following values: _self, _blank, _parent, and _top:

ALTER TABLE links 
ADD CHECK (target IN ('_self', '_blank', '_parent', '_top'));

